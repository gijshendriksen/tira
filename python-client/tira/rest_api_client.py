import requests
import json
import pandas as pd

class Client():
    def __init__(self, api_key):
        self.__api_key = api_key
        self.fail_if_api_key_is_invalid()

    def fail_if_api_key_is_invalid(self):
        role = self.json_response('/api/role')
        
        if not role or 'status' not in role or 'role' not in role or 0 != role['status']:
            raise ValueError('It seems like the api key is invalid. Got: ', role)

    def datasets(self, task):
        return json.loads(self.json_response(f'/api/datasets_by_task/{task}')['context']['datasets'])

    def submissions(self, task, dataset):
        response = self.json_response(f'/api/submissions/{task}/{dataset}')['context']
        ret = []
        
        for vm in response['vms']:
            for run in vm['runs']:
                for k,v in run['review'].items():
                    run['review_' + k] = v
                del run['review']

                ret += [{**{'task': response['task_id'], 'dataset': response['dataset_id'], 'team': vm['vm_id']}, **run}]

        return pd.DataFrame(ret)

    def evaluations(self, task, dataset, join_submissions=True):
        response = self.json_response(f'/api/evaluations/{task}/{dataset}')['context']
        ret = []
        evaluation_keys = response['ev_keys']

        if join_submissions:
            runs_to_join = {}
            for _, i in self.submissions(task, dataset).iterrows():
                i = i.to_dict()
                runs_to_join[(i['team'], i['run_id'])] = {'software': i['software'], 'is_upload': i['is_upload'], 'is_docker': i['is_docker']}

        for evaluation in response['evaluations']:
            run = {'task': response['task_id'], 'dataset': response['dataset_id'], 'team': evaluation['vm_id'], 'run_id': evaluation['input_run_id']}

            if join_submissions:
                software = runs_to_join[(run['team'], run['run_id'])]
                for k,v in software.items():
                    run[k] = v

            for measure_id, measure in zip(range(len(evaluation_keys)), evaluation_keys):
                run[measure] = evaluation['measures'][measure_id]

            ret += [run]

        return pd.DataFrame(ret)

    def json_response(self, endpoint, params=None):
        headers = {"Api-Key": self.__api_key, "Accept": "application/json"}
        resp = requests.get(url='https://www.tira.io' + endpoint, headers=headers, params=params)
        
        return resp.json()
