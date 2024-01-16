FROM python:3.8-slim-buster

WORKDIR /home/yang/GEE/Project_gee_docker/Project_gee_2




COPY requirements.txt /home/yang/GEE/Project_gee_docker/Project_gee_2/requirements.txt

RUN python3 -m pip install -r /home/yang/GEE/Project_gee_docker/Project_gee_2/requirements.txt

RUN apt-get update && apt-get install -y curl gnupg
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
RUN apt-get update && apt-get install -y google-cloud-sdk

RUN     pip install --upgrade oauth2client
RUN     pip install --upgrade six


RUN curl -sSL https://sdk.cloud.google.com | bash

ADD . /home/yang/GEE/Project_gee_docker/Project_gee_2

CMD ["python", "/home/yang/GEE/Project_gee_docker/Project_gee_2/run.py"]
