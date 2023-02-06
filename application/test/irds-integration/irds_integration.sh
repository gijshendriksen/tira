#!/bin/sh

docker run --rm -ti \
    -v /mnt/ceph/storage/corpora/corpora-thirdparty:/mnt/ceph/storage/corpora/corpora-thirdparty:ro \
    -v /mnt/ceph/tira/state/ir_datasets:/root/.ir_datasets \
    -v /mnt/ceph/tira/data/datasets/:/mnt/ceph/tira/data/datasets/ \
    -v ${PWD}/cw09-integration/:/tmp-out/
    --entrypoint /irds_cli.sh webis/tira-application:0.0.34 \
        --input_dataset_directory /mnt/ceph/tira/data/datasets/training-datasets/ir-benchmarks/clueweb09-en-trec-web-2009-20230107-training/ \
        --output_dataset_path $outputDir /tmp-out/web-09-rerank --rerank /tmp-out/web-09-run

