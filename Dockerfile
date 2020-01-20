FROM tensorflow/tensorflow:1.13.1-gpu-py3

# COPY and ADD copies only the contents of the folder, not the folder.
COPY ./ /ner-trainer

WORKDIR /ner-trainer

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -U pip
#RUN python setup.py install
RUN pip install -r requirement.txt

RUN chmod u+x ./train_eval.sh
RUN chmod u+x ./service_startup.sh

ENTRYPOINT ["bash"]

