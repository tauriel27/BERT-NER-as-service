#!/bin/bash
ROOT_DIR=./BERT-BiLSTM-CRF-NER
BERT_MODEL_DIR=$ROOT_DIR/roberta_zh_l12

data_dir=$1
gpu=$2

python train_eval.py \
    -bert_config_file $BERT_MODEL_DIR/bert_config.json \
    -output_dir $ROOT_DIR/output/ \
    -init_checkpoint $BERT_MODEL_DIR/bert_model.ckpt \
    -vocab_file $BERT_MODEL_DIR/vocab.txt \
    -max_seq_length 128 \
    -data_dir $data_dir \
    -num_train_epochs 1 \
    -save_checkpoints_steps 1000 \
    -save_summary_steps 500 \
    -batch_size 64 \
    -do_train \
    -do_eval \
    -do_predict \
    -device_map $gpu \
    -learning_rate 5e-5 \
    -dropout_rate 0.9 \
    -crf