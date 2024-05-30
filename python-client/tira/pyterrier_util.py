from pyterrier.transformer import Transformer, SourceTransformer
import json
import pandas as pd
import tempfile
import gzip
import os
from typing import Mapping, Iterable


def merge_runs(topics, run_file):
    import numpy as np
    df = pd.read_csv(run_file, sep='\\s+', names=["qid", "q0", "docno", "rank", "score", "system"])
    df['qid'] = df['qid'].astype(str)
    df['docno'] = df['docno'].astype(str)
    topics['qid'] = topics['qid'].astype(str)

    common_columns = np.intersect1d(topics.columns, df.columns)
    join_on = ["qid", "docno"] if 'qid' in common_columns and 'docno' in common_columns else ['qid']

    # we drop columns in topics that exist in the df
    keeping = topics.columns
    drop_columns = [i for i in common_columns if i not in {"qid", "docno"}]
    if len(drop_columns) > 0:
        keeping = topics.columns[~ topics.columns.isin(drop_columns)]

    return topics[keeping].merge(df, how='left', left_on=join_on, right_on=join_on)


class TiraSourceTransformer(SourceTransformer):
    def __init__(self, rtr, **kwargs):
        super().__init__(rtr, **kwargs)

    
    def transform(self, topics):
        import numpy as np
        if 'docno' not in topics.columns:
            return super().transform(topics)
        elif 'qid' not in topics.columns:
            raise ValueError('The dataframe needs to have a column "qid"')
        
        keeping = topics.columns

        common_columns = np.intersect1d(topics.columns, self.df.columns)

        # we drop columns in topics that exist in the self.df
        drop_columns = [i for i in common_columns if i not in ("qid", "docno")]
        if len(drop_columns) > 0:
            keeping = topics.columns[~ topics.columns.isin(drop_columns)]

        return topics[keeping].merge(self.df, on=["qid", "docno"])

class TiraFullRankTransformer(Transformer):
    """
    A Transformer that re-executes some full-rank approach submitted to a shared task in TIRA.
    """

    def __init__(self, approach, tira_client, input_dir, **kwargs):
        self.approach = approach
        self.tira_client = tira_client
        self.input_dir = input_dir

    def transform(self, topics):
        output_dir = tempfile.TemporaryDirectory('-pt-tira-local-execution-full-rank-transformer').name + '/output'
        os.makedirs(output_dir)

        self.tira_client.local_execution.run(identifier=self.approach,
            input_dir=self.input_dir, output_dir=output_dir,
            evaluate=False, dry_run=False
        )

        return merge_runs(topics, output_dir + '/run.txt')


class TiraRerankingTransformer(Transformer):
    """
    A Transformer that loads runs from TIRA that reranked some existing run.
    """

    def __init__(self, approach, tira_client, dataset=None, datasets=None, **kwargs):
        self.task, self.team, self.software = approach.split('/')
        self.tira_client = tira_client
        from tira.ir_datasets_util import translate_irds_id_to_tirex
        if dataset and datasets:
            raise ValueError(f'You can not pass both, dataset and datasets. Got dataset = {dataset} and datasets= {datasets}')

        if not datasets and dataset:
            datasets = [dataset]
        self.datasets = datasets
        
        if self.datasets:
            self.datasets = [translate_irds_id_to_tirex(i) for i in self.datasets]

    def transform(self, topics):
        import numpy as np
        assert "qid" in topics.columns

        if 'tira_task' not in topics.columns or 'tira_dataset' not in topics.columns or 'tira_first_stage_run_id' not in topics.columns:
            if self.datasets:
                tira_configurations = [{'tira_task': self.task, 'tira_dataset': i, 'tira_first_stage_run_id': None} for i in self.datasets]
            else:
                raise ValueError('This run needs to know the tira metadata: tira_task, tira_dataset, and tira_first_stage_run_id needs to be in the columns of the dataframe')
        else:
            tira_configurations = [json.loads(i) for i in topics[['tira_task', 'tira_dataset', 'tira_first_stage_run_id']].apply(lambda i: json.dumps(i.to_dict()), axis=1).unique()]

        df = []
        for tira_configuration in tira_configurations:
            df += [self.tira_client.download_run(tira_configuration['tira_task'], tira_configuration['tira_dataset'], self.software, self.team, tira_configuration['tira_first_stage_run_id'])]
        df = pd.concat(df)
        df['qid'] = df['query'].astype(str)
        df['docno'] = df['docid'].astype(str)
        del df['query']
        del df['docid']

        common_columns = np.intersect1d(topics.columns, df.columns)

        # we drop columns in topics that exist in the df
        keeping = topics.columns
        drop_columns = [i for i in common_columns if i not in {"qid", "docno"}]
        if len(drop_columns) > 0:
            keeping = topics.columns[~ topics.columns.isin(drop_columns)]

        join_criterium = ['qid'] if 'docno' not in keeping else ['qid', 'docno']
        return topics[keeping].merge(df, how='left', left_on=join_criterium, right_on=join_criterium)


class TiraLocalExecutionRerankingTransformer(Transformer):
    """
    A Transformer that re-execues software submitted in TIRA.
    """

    def __init__(self, approach, tira_client, irds_id=None, **kwargs):
        self.task, self.team, self.software = approach.split('/')
        self.approach = approach
        self.tira_client = tira_client
        self.irds_id = irds_id

    def transform(self, topics):
        assert "qid" in topics.columns

        tmp_directory = tempfile.TemporaryDirectory('-pt-tira-local-execution-reranking-transformer').name
        input_dir = self.tira_client.pt.create_rerank_file(run_df=topics, irds_dataset_id=self.irds_id)
        output_dir = tmp_directory + '/output'
        os.makedirs(output_dir)

        self.tira_client.local_execution.run(identifier=self.approach,
            input_dir=input_dir, output_dir=output_dir,
            evaluate=False, dry_run=False
        )

        return merge_runs(topics, tmp_directory + '/output/run.txt')


class TiraApplyFeatureTransformer(Transformer):
    """
    A Transformer that takes a mapping of values (e.g. docids or qids) to features, and applies this
    mapping to each row of the dataframe to obtain the right feature value or vector for that row.

    The `id_cols` parameter specifies the columns that are used to identify the right feature for a row.
    For instance:
    - For query-only features, we set `id_cols` = ('qid',) and the output feature will be `mapping[row['qid']]`.
    - For document-only features, we set `id_cols` = ('docno',) and the output feature will be `mapping[row['docno']]`.
    - For query-document features, we set `id_cols` = ('qid', 'docno') and the output feature will be `mapping[row['qid']][row['docno']]`.
    """

    def __init__(self, mapping: Mapping, id_cols: Iterable[str] = ('qid', 'docno'), name: str = 'apply_features') -> None:
        self.mapping = mapping
        self.id_cols = id_cols
        self.name = name

    def __repr__(self):
        return f'tira.pt.{self.name}()'

    def transform(self, inputRes):
        outputRes = inputRes.copy()
        outputRes["features"] = outputRes.apply(self._get_features_from_row, axis=1)
        return outputRes

    def _get_features_from_row(self, row):
        value = self.mapping
        for col in self.id_cols:
            value = value[str(row[col])]

        return value


class TiraNamedFeatureTransformer(Transformer):
    def __init__(self, feature_transformer: Transformer, feature_names: str | list[str], feature_categories: str | list[str] | None = None):
        self.feature_transformer = feature_transformer
        self.feature_names = feature_names if isinstance(feature_names, list) else [feature_names]
        self.feature_categories = feature_categories if isinstance(feature_categories, list) else [feature_categories for _ in self.feature_names]

        assert len(self.feature_names) == len(self.feature_categories), f'\n{self.feature_names}\n{self.feature_categories}'

    def __pow__(self, right: Transformer) -> Transformer:
        if isinstance(right, TiraNamedFeatureTransformer):
            return TiraNamedFeatureTransformer(
                self.feature_transformer ** right.feature_transformer,
                self.feature_names + right.feature_names,
                self.feature_categories + right.feature_categories,
            )

        return TiraNamedFeatureTransformer(self.feature_transformer ** right, self.feature_names + [str(right)], self.feature_categories + [None])

    def transform(self, topics):
        return self.feature_transformer.transform(topics)
