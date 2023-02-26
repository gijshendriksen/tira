import os
import docker
from copy import deepcopy


class LocalExecutionIntegration():
    def __init__(self, tira_client):
        self.tira_client = tira_client

    def __normalize_command(self, cmd):
        to_normalize = {'inputRun': '/tira-data/output',
                        'outputDir': '/tira-data/output',
                        'inputDataset': '/tira-data/input'
                       }

        if 'inputRun' in cmd:
            to_normalize['outputDir'] = '/tira-data/eval_output'
            to_normalize['inputDataset'] = '/tira-data/input_truth'
    
        for k,v in to_normalize.items():
            cmd = cmd.replace('$' + k, v).replace('${' + k + '}', v)
    
        return cmd

    def run(self, identifier=None, image=None, command=None, input_dir=None, output_dir=None, evaluate=False, verbose=False, dry_run=False, docker_software_id_to_output=None):
        if image is None or command is None:
            ds = self.tira_client.docker_software(identifier)
            image, command, s_id, previous_stages = ds['tira_image_name'], ds['command'], ds['id'], ds['ids_of_previous_stages']
        if not dry_run:
            try:
                client = docker.from_env()
        
                assert len(client.images.list()) >= 0
                assert len(client.containers.list()) >= 0
            except Exception as e:
                raise ValueError('It seems like docker is not installed?', e)

        command = self.__normalize_command(command)
    
        if not input_dir or not output_dir:
            raise ValueError('please pass input_dir and output_dir')
    
        input_dir = os.path.abspath(input_dir)
        output_dir = os.path.abspath(output_dir)
    
        docker_software_id_to_output = {} if not docker_software_id_to_output else deepcopy(docker_software_id_to_output)
        for previous_stage in previous_stages:
            if previous_stage in docker_software_id_to_output.keys():
                continue

            tmp_ds = self.tira_client.docker_software(approach=None, software_id=previous_stage)

            tmp_prev_stages = run(self, identifier=None, image=tmp_ds['tira_image_name'], command=tmp_ds['command'],
                                  input_dir=input_dir, evaluate=False, verbose=verbose, dry_run=dry_run,
                                  output_dir=tempfile.TemporaryDirectory('-staged-execution-' + previous_stage).name + '/output', 
                                  docker_software_id_to_output=docker_software_id_to_output
                                 )
            for k, v in tmp_prev_stages.items():
                docker_software_id_to_output[k] = v
    
        if verbose:
            print(f'docker run --rm -ti -v {input_dir}:/tira-data/input:ro -v {output_dir}:/tira-data/output:rw --entrypoint sh {image} -c \'{command}\'')
    
        if dry_run:
            return
    
        client.containers.run(image, entrypoint='sh', command=f'-c "{command}"', volumes={
            str(input_dir): {'bind': '/tira-data/input', 'mode': 'ro'},
            str(output_dir): {'bind': '/tira-data/output', 'mode': 'rw'}
        })

        if evaluate:
            if type(evaluate) is not str:
                evaluate = data
            evaluate, image, command = __extract_image_and_command(evaluate, evaluator=True)
            command = __normalize_command(command)
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

