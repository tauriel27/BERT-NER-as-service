# NER-server
包含NER模型的训练、评估、服务启动、部署。\
代码整理自[BERT-BiLSTM-CRF-NER](https://github.com/macanv/BERT-BiLSTM-CRF-NER).

# 安装
```bash
pip install -r requirement.txt
```

# 脚本运行
## 训练评估
> 该过程会训练模型，并保存模型文件，然后跟baseline model进行对比评估。
```bash
sh train_eval.sh DATA_DIR GPU_ID
```
- 输入 
    - BERT_MODEL_DIR： 预训练模型地址，应该包含config file、vocab file、chechpoint。
- 输出 \
模型输出checkpoint和测试集预测结果，位置 `/data/NER`。

## NER服务启动
> 启动NER服务，用户可以通过客户端发送文本并返回实体标注序列。
```bash
sh service_startup.sh
```
- 输入 
    - model_dir：fine-tuned后的模型地址
    - bert_model_dir：预训练模型地址（只使用配置文件和词表）
- 输出 \
当前文件夹会产生模型压缩文件predict_optimizer。 `/data/tmp`会产生缓存文件。服务结束可以删除。

# Docker运行
## 训练评估
```bash
docker build -t $IMAGE_NAME:$TAG -f $DOCKERFILE .
docker run --gpus all --rm -d -v /data:/data --name ner-trainer $IMAGE_NAME:$TAG train_eval.sh $DATA_DIR $GPU_ID
```
## NER服务启动
```bash
docker run --gpus all -d -v /data:/data -p 0.0.0.0:5555:5555 -p 0.0.0.0:5556:5556 --name ner-server $IMAGE_NAME:$TAG service_startup.sh
```
