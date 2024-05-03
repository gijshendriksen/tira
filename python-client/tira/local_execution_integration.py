import os
import sys
import docker
import json
from copy import deepcopy
import tempfile
import subprocess
import tarfile
import logging
from pathlib import Path
import pandas as pd


class LocalExecutionIntegration():
    def __init__(self, tira_client=None):
        self.tira_client = tira_client

    def __normalize_command(self, cmd, evaluator):
        to_normalize = {'inputRun': '/tira-data/input-run',
                        'outputDir': '/tira-data/output',
                        'inputDataset': '/tira-data/input'
                       }

        if 'inputRun' in cmd and evaluator:
            to_normalize['outputDir'] = '/tira-data/eval_output'
            to_normalize['inputDataset'] = '/tira-data/input_truth'

        for k, v in to_normalize.items():
            cmd = cmd.replace('$' + k, v).replace('${' + k + '}', v)

        return cmd

    def __normalize_path(self, path):
        beheaded_path = path if not str(path).startswith('$PWD') else str(path)[4:]
        beheaded_path = os.path.abspath(".") if len(beheaded_path) == 0 or beheaded_path in ['/', '.'] else \
            beheaded_path[0].replace('/', '') + beheaded_path[1:]
        return beheaded_path

    def construct_verbosity_output(self, input_dir, output_dir, image, command, original_args):
        beheaded_input_dir = self.__normalize_path(input_dir)
        beheaded_output_dir = self.__normalize_path(output_dir)
        tira_run_input_dir = beheaded_input_dir if not str(beheaded_input_dir) == str(os.path.abspath(".")) else None
        tira_run_output_dir = beheaded_output_dir if not str(beheaded_output_dir) == str(os.path.abspath("tira-output")) else None
        tira_run_python_args = {k: v for k, v in original_args.items()}
        if type(tira_run_python_args['input_dir']) is str and tira_run_python_args['input_dir'].startswith('$PWD'):
            tira_run_python_args['input_dir'] = self.__normalize_path(tira_run_python_args['input_dir'])
        if type(tira_run_python_args['output_dir']) is str and tira_run_python_args['output_dir'].startswith('$PWD'):
            tira_run_python_args['output_dir'] = self.__normalize_path(tira_run_python_args['output_dir'])
        tira_run_args = [(k, v if type(v) is not str else f'"{v}"') for k, v in tira_run_python_args.items()]
        tira_run_args = [i.strip() for i in ['' if not tira_run_python_args[k] else f'{k}={v}' for k, v in tira_run_args] if i]

        return {
            'tira-run-cli': 'tira-run ' +
                ('' if not tira_run_input_dir else f'--input-directory {tira_run_input_dir} ') +
                ('' if not tira_run_output_dir else f'--output-directory {tira_run_output_dir} ') +
                (f'--approach {original_args["identifier"]} ' if 'identifier' in original_args and original_args['identifier'] is not None else f'--image {image} --command \'{original_args["command"]}\''),

            'tira-run-python': 'tira.run(' +
                (', '.join(tira_run_args))
            + ')',

            'docker': f'docker run --rm -ti -v {input_dir}:/tira-data/input:ro -v {output_dir}:/tira-data/output:rw --entrypoint sh {image} -c \'{command}\''
        }

    def ensure_image_available_locally(self, image, client=None):
        try:
            output = subprocess.check_output(['docker', 'images', '-q', image])
            if len(output) > 0:
                return
        except Exception:
            pass

        if client:
            try:
                if any(image in str(i) for i in client.images.list()):
                    return
            except Exception:
                pass

        print('# Pull Image\n\n')
        image_pull_code = subprocess.call(['docker', 'pull', image])

        if image_pull_code != 0 and 'GITHUB_ACTION' in os.environ:
            print("Skip pulling of image because everything is executed within github.")
            return

        if image_pull_code != 0:
            raise ValueError(f'Image could not be successfully pulled. Got return code {image_pull_code}. (expected 0.)')

        print('\n\n Image pulled successfully.\n\nI will now run the software.\n\n')

    def extract_entrypoint(self, image):
        image_name = image
        self.ensure_image_available_locally(image_name)
        image = self.__docker_client().images.get(image_name)
        ret = image.attrs['Config']['Entrypoint']
        if not ret:
            return None

        for i in deepcopy(ret):
            if i.startswith('[') and i.endswith(']'):
                print(i)
                ret = json.loads(i)
                break

        return self.make_command_absolute(image_name, ' '.join(ret))

    def make_command_absolute(self, image_name, command):
        from tira.third_party_integrations import extract_to_be_executed_notebook_from_command_or_none
        executable = extract_to_be_executed_notebook_from_command_or_none(command)

        if not executable or executable.startswith('/') or executable.startswith("'/") or executable.startswith('"/'):
            return command
        else:
            return command.replace(executable, (self.docker_image_work_dir(image_name) + '/' + executable).replace('//', '/').replace('/./', '/'))

    def __docker_client(self):
        try:
            environ = os.environ.copy()
            if sys.platform == "linux" and os.path.exists(os.path.expanduser("~/.docker/desktop/docker.sock")):
                environ["DOCKER_HOST"] = "unix:///" + os.path.expanduser("~/.docker/desktop/docker.sock")
            client = docker.from_env(environment=environ)

            assert len(client.images.list()) >= 0
            assert len(client.containers.list()) >= 0
            return client
        except Exception as e:
            raise ValueError('It seems like docker is not installed?', e)

    def docker_client_is_authenticated(self, client=None):
        if not client:
            client = self.__docker_client()

        auth_config = client.api._auth_configs
        if not self.tira_client.docker_registry() or 'auths' not in auth_config  or self.tira_client.docker_registry() not in auth_config['auths']:
            return False

        auth_config = auth_config['auths'][self.tira_client.docker_registry()]

        if not auth_config or 'username' not in auth_config or 'password' not in auth_config:
            return False

        login_response = client.login(username=auth_config['username'], password=auth_config['password'], registry=self.tira_client.docker_registry())

        return ('username' in login_response and 'password' in login_response and auth_config['username'] == login_response['username'] and auth_config['password'] == login_response['password']) or ('Status' in login_response and 'login succeeded' == login_response['Status'].lower())

    def login_docker_client(self, task_name, team_name, client=None):
        if not client:
            client = self.__docker_client()

        if self.docker_client_is_authenticated(client):
            return True

        docker_user, docker_password, docker_registry = self.tira_client.docker_credentials(task_name, team_name)

        if not docker_user or not docker_password or not docker_registry:
            print('Please login. Run "tira-cli login --token YOUR-TOKEN-HERE"')
            raise ValueError('Please login. Run "tira-cli login --token YOUR-TOKEN-HERE"')

        #print('Login: ', docker_user, docker_password, docker_registry)
        login_response = client.login(username=docker_user, password=docker_password, registry=docker_registry)

        if 'Status' not in login_response or 'login succeeded' != login_response['Status'].lower():
            print('Credentials are not valid, please run "tira-cli login --token YOUR-TOKEN-HERE"')
            raise ValueError(f'Login was not successfull, got: {login_response}')
    
        return True


    def run(self, identifier=None, image=None, command=None, input_dir=None, output_dir=None, evaluate=False, dry_run=False, docker_software_id_to_output=None, software_id=None, allow_network=False, input_run=None, additional_volumes=None, eval_dir='tira-evaluation', gpu_count=0):
        previous_stages = []
        original_args = {'identifier': identifier, 'image': image, 'command': command, 'input_dir': input_dir, 'output_dir': output_dir, 'evaluate': evaluate, 'dry_run': dry_run, 'docker_software_id_to_output': docker_software_id_to_output, 'software_id': software_id}
        s_id = 'unknown-software-id'
        if image is None or command is None:
            ds = self.tira_client.docker_software(approach=identifier, software_id=software_id)
            image, command, s_id, previous_stages = ds['tira_image_name'], ds['command'], ds['id'], ds['ids_of_previous_stages']
        if not dry_run:
            client = self.__docker_client()

        command = self.__normalize_command(command, False)

        if not input_dir or not output_dir:
            raise ValueError('please pass input_dir and output_dir')

        input_dir = os.path.abspath(input_dir) if not str(input_dir).startswith('$PWD') else input_dir
        output_dir = os.path.abspath(output_dir) if not str(output_dir).startswith('$PWD') else output_dir

        docker_software_id_to_output = {} if not docker_software_id_to_output else deepcopy(docker_software_id_to_output)

        for previous_stage in previous_stages:
            if previous_stage in docker_software_id_to_output.keys():
                continue

            tmp_prev_stages = self.run(software_id=previous_stage, identifier=None, image=None, command=None,
                                       input_dir=input_dir, evaluate=False, dry_run=dry_run,
                                       output_dir=tempfile.TemporaryDirectory('-staged-execution-' + previous_stage).name + '/output', 
                                       docker_software_id_to_output=docker_software_id_to_output
                                )
            for k, v in tmp_prev_stages.items():
                docker_software_id_to_output[k] = v
    
        verbose_data = self.construct_verbosity_output(input_dir, output_dir, image, command, original_args)
        logging.debug(f'Docker:\n\t{verbose_data["docker"]}\n\ntira-run (python):\n\t{verbose_data["tira-run-python"]}\n\ntira-run (CLI):\n\t{verbose_data["tira-run-cli"]}\n\n')
    
        if dry_run:
            return verbose_data

        volumes = {
            str(input_dir): {'bind': '/tira-data/input', 'mode': 'ro'},
            str(output_dir): {'bind': '/tira-data/output', 'mode': 'rw'},
        }
        
        if input_run:
            volumes[str(input_run)] = {'bind': '/tira-data/input-run', 'mode': 'ro'}
        
        for k, v in docker_software_id_to_output.items():
            volumes[str(os.path.abspath(v))] = {'bind': '/tira-data/input-run', 'mode': 'ro'}

        if additional_volumes:
            for v in additional_volumes:
                volume_dir, volume_bind, volume_mode = v.split(':')
                volume_dir = str(os.path.abspath(volume_dir))
                if volume_dir in volumes:
                    raise ValueError(f'Volume to mount is multiple times defined: {volume_dir}')
                volumes[volume_dir] = {'bind': volume_bind, 'mode': volume_mode}

        self.ensure_image_available_locally(image, client)
        environment = {'outputDir': '/tira-data/output', 'inputDataset': '/tira-data/input', 'TIRA_DATASET_ID': 'id', 'TIRA_OUTPUT_DIR': '/tira-data/output', 'TIRA_INPUT_DATASET': '/tira-data/input'}

        if input_run:
            environment['inputRun'] = '/tira-data/input-run'

        device_requests = []
        if gpu_count != 0:
            device_requests=[docker.types.DeviceRequest(count=gpu_count, capabilities=[['gpu']])]

        container = client.containers.run(image, entrypoint='sh', command=f'-c "{command}; sleep .1"', environment=environment, volumes=volumes, detach=True, remove=True, network_disabled = not allow_network, device_requests=device_requests)

        for line in container.attach(stdout=True, stream=True, logs=True):
            print(line.decode('utf-8'))

        if evaluate:
            evaluation_volumes = {str(eval_dir): {'bind': '/tira-data/eval_output', 'mode': 'rw'}}

            if type(evaluate) is dict and evaluate['evaluator_id']:
                evaluation_volumes[str(evaluate['truth_directory'])] = {'bind': '/tira-data/input_truth', 'mode': 'ro'}
                evaluation_volumes[str(output_dir)] = {'bind': '/tira-data/input-run', 'mode': 'ro'}
                
                evaluate, image, command = None, evaluate['evaluator_git_runner_image'],  evaluate['evaluator_git_runner_command']
            elif type(evaluate) is not str:
                evaluate = data

            if image == None or command == None:
                evaluate, image, command = __extract_image_and_command(evaluate, evaluator=True)

            command = self.__normalize_command(command, True)
            logging.debug(f'Evaluate software with: docker run --rm -ti -v {input_dir}:/tira-data/input -v {output_dir}/:/tira-data/output --entrypoint sh {image} -c \'{command}\'')
        
            container = client.containers.run(image, entrypoint='sh', command=f'-c "{command}; sleep .1"', volumes=evaluation_volumes, detach=True, remove=True, network_disabled = not allow_network)

            for line in container.attach(stdout=True, stream=True, logs=True):
                print(line.decode('utf-8'), flush=True)

        if evaluate:
            approach_name = identifier if identifier else f'"{command}"@{image}'
            eval_results = {'approach': approach_name, 'evaluate': evaluate}
            eval_results.update(self.load_output_of_directory(Path(eval_dir), evaluation=True))
            return self.load_output_of_directory(Path(eval_dir)), pd.DataFrame([eval_results])
        else:
            docker_software_id_to_output[s_id] = output_dir
            return docker_software_id_to_output

    def docker_image_work_dir(self, image):
        image = self.__docker_client().images.get(image).attrs['Config']
        return '/' + image.get('WorkingDir', '')

    def export_file_from_software(self, container_path, host_path, identifier=None, image=None, software_id=None):
        """
        Export a file specified by container_path' from a software to the host_path at the host.
        """
        if image is None:
            ds = self.tira_client.docker_software(approach=identifier, software_id=software_id)
            image = ds['tira_image_name']

        client = self.__docker_client()
        self.ensure_image_available_locally(image, client)
        docker_container = client.containers.create(image)
        strm, stat = docker_container.get_archive(container_path, None)

        with open(host_path, 'wb') as f:
            for i in strm:
                f.write(i)

        tf = tarfile.open(host_path, mode='r')
        tf = tf.extractfile(stat[u'name']).read()

        with open(host_path, 'wb') as f:
            f.write(tf)

        docker_container.remove()

    def export_submission_from_jupyter_notebook(self, notebook):
        if not os.path.isfile(notebook):
            print(f'The notebook {notebook} does not exist. I can not continue.', file=sys.stderr)

            if '/' in notebook:
                try:
                    notebook = '/'.join(notebook.split('/')[:-1])
                    print(f'The directory {notebook} contains the files {os.listdir(notebook)}. Maybe you did mean one of those?', file=sys.stderr)
                except:
                    pass

            return None

        ret = []

        ret += ['TIRA_COMMAND=/workspace/run-pyterrier-notebook.py --input ${TIRA_INPUT_DIRECTORY} --output ${TIRA_OUTPUT_DIRECTORY} --notebook /workspace/' + notebook.split("/")[-1]]
        notebook_content = json.load(open(notebook, 'r'))

        return '\n'.join(ret)

    def normalize_image_name(self, image, required_prefix):
        if required_prefix and not image.startswith(required_prefix):
            ret = (required_prefix + '/' + (image + ':').split(':')[0][:10]).replace('//', '/') + ':' + (image.split(':')[-1] if ':' in image else 'latest')
            return ret.replace('-:', ':').replace('::', ':').replace('/:', ':')
        else:
            return image

    def show_docker_progress(self, line, tasks):
        from tqdm import tqdm

        if 'status' not in line or (line['status'] != 'Downloading' and line['status'] != 'Extracting' and line['status'] != 'Pushing'):
            # skip other statuses
            return

        id = f'{line["id"]}--{line["status"]}'

        if id not in tasks:
            tasks[id] = tqdm(position=len(tasks) +1, desc=f'{line["status"]} ({line["id"]}):')

        try:
            tasks[id].update(line['progressDetail']['total'])
        except:
            pass

    def push_image(self, image, required_prefix=None, task_name=None, team_name=None):
        client = self.__docker_client()
        if not self.docker_client_is_authenticated(client):
            self.login_docker_client(task_name, team_name, client)
        new_image = image
        if required_prefix and not image.startswith(required_prefix):
            new_image = self.normalize_image_name(image, required_prefix)
            print(f'I tag the image "{image}" as "{new_image}" for upload to TIRA (only internal).')
            client.images.get(image).tag(new_image)
            image = new_image

        tasks = {}
        push_response = ''
        for line in client.images.push(image, stream=True, decode=True):
            push_response += str(line)
            self.show_docker_progress(line, tasks)

        if 'error' in push_response:
            raise ValueError('Could not push image')
        return new_image
