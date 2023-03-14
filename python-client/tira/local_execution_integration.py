import os
import docker
from copy import deepcopy
import tempfile


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
    
        for k,v in to_normalize.items():
            cmd = cmd.replace('$' + k, v).replace('${' + k + '}', v)
    
        return cmd

    def construct_verbosity_output(self, input_dir, output_dir, image, command, original_args):
        tira_run_input_dir = input_dir if not str(input_dir) == str(os.path.abspath(".")) else None
        tira_run_output_dir = output_dir if not str(output_dir) == str(os.path.abspath("tira-output")) else None
        tira_run_args = [(k, v if type(v) is not str else f'"{v}"') for k, v in original_args.items()]
        tira_run_args = [i.strip() for i in ['' if not original_args[k] else f'{k}={v}' for k, v in tira_run_args] if i]
    
        return {
            'tira-run-cli': f'tira-run ' + 
                ('' if not tira_run_input_dir else f'--input-directory {tira_run_input_dir} ') +
                ('' if not tira_run_output_dir else f'--output-directory {tira_run_output_dir} ') + 
                (f'--approach {original_args["identifier"]} ' if 'identifier' in original_args else f'--image {image} --command \'{original_args["command"]}\''),

            'tira-run-python': 'tira.run(' + 
                (', '.join(tira_run_args))
            + ')',

            'docker': f'docker run --rm -ti -v {input_dir}:/tira-data/input:ro -v {output_dir}:/tira-data/output:rw --entrypoint sh {image} -c \'{command}\''
        }

    def run(self, identifier=None, image=None, command=None, input_dir=None, output_dir=None, evaluate=False, verbose=False, dry_run=False, docker_software_id_to_output=None, software_id=None):
        previous_stages = []
        original_args = {'identifier': identifier, 'image': image, 'command': command, 'input_dir': input_dir, 'output_dir': output_dir, 'evaluate': evaluate, 'verbose': verbose, 'dry_run': dry_run, 'docker_software_id_to_output': docker_software_id_to_output, 'software_id': software_id}
        s_id = 'unknown-software-id'
        if image is None or command is None:
            ds = self.tira_client.docker_software(approach=identifier, software_id=software_id)
            image, command, s_id, previous_stages = ds['tira_image_name'], ds['command'], ds['id'], ds['ids_of_previous_stages']
        if not dry_run:
            try:
                client = docker.from_env()
        
                assert len(client.images.list()) >= 0
                assert len(client.containers.list()) >= 0
            except Exception as e:
                raise ValueError('It seems like docker is not installed?', e)

        command = self.__normalize_command(command, False)
    
        if not input_dir or not output_dir:
            raise ValueError('please pass input_dir and output_dir')
    
        input_dir = os.path.abspath(input_dir)
        output_dir = os.path.abspath(output_dir)
    
        docker_software_id_to_output = {} if not docker_software_id_to_output else deepcopy(docker_software_id_to_output)

        for previous_stage in previous_stages:
            if previous_stage in docker_software_id_to_output.keys():
                continue

            tmp_prev_stages = self.run(software_id=previous_stage, identifier=None, image=None, command=None,
                                  input_dir=input_dir, evaluate=False, verbose=verbose, dry_run=dry_run,
                                  output_dir=tempfile.TemporaryDirectory('-staged-execution-' + previous_stage).name + '/output', 
                                  docker_software_id_to_output=docker_software_id_to_output
                                 )
            for k, v in tmp_prev_stages.items():
                docker_software_id_to_output[k] = v
    
        verbose_data = self.construct_verbosity_output(input_dir, output_dir, image, command, original_args)
        if verbose:
            print(f'Docker:\n\t{verbose_data["docker"]}\n\ntira-run (python):\n\t{verbose_data["tira-run-python"]}\n\ntira-run (CLI):\n\t{verbose_data["tira-run-cli"]}\n\n')
    
        if dry_run:
            return verbose_data

        volumes = {
            str(input_dir): {'bind': '/tira-data/input', 'mode': 'ro'},
            str(output_dir): {'bind': '/tira-data/output', 'mode': 'rw'},
        }
        
        for k, v in docker_software_id_to_output.items():
            volumes[str(os.path.abspath(v))] = {'bind': '/tira-data/input-run', 'mode': 'ro'}

        container = client.containers.run(image, entrypoint='sh', command=f'-c "{command}"', volumes=volumes, detach=True, remove=True)

        for line in container.attach(stdout=True, stream=True, logs=True):
            print(line.decode('utf-8'), flush=True)

        if evaluate:
            if type(evaluate) is not str:
                evaluate = data
            evaluate, image, command = __extract_image_and_command(evaluate, evaluator=True)
            command = __normalize_command(command, True)
            if verbose:
                print(f'Evaluate software with: docker run --rm -ti -v {input_dir}:/tira-data/input -v {output_dir}/:/tira-data/output --entrypoint sh {image} -c \'{command}\'')
        
            client.containers.run(image, entrypoint='sh', command=f'-c "{command}"', volumes={str(data_dir): {'bind': '/tira-data/', 'mode': 'rw'}})

        if evaluate:
            approach_name = identifier if identifier else f'"{command}"@{image}'
            eval_results = {'approach': approach_name, 'evaluate': evaluate}
            eval_results.update(load_output_of_directory(Path(data_dir) / 'eval_output', evaluation=True, verbose=verbose))
            return load_output_of_directory(Path(data_dir) / 'output', verbose=verbose), pd.DataFrame([eval_results])
        else:
            docker_software_id_to_output[s_id] = output_dir
            return docker_software_id_to_output

