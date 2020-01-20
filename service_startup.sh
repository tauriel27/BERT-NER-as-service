#!/bin/bash
ROOT_DIR=./BERT-BiLSTM-CRF-NER

rm -rf $ROOT_DIR/predict_optimizer
export ZEROMQ_SOCK_TMP_DIR=/data/tmp

python start_server.py \
    -model_dir $ROOT_DIR/baseline \
    -bert_model_dir $ROOT_DIR/roberta_zh_l12 \
    -mode NER \
    -max_seq_len 128 \
    -max_batch_size 512 \
    -device_map 1 \
    -crf


