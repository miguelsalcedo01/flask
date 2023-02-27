FROM python:3.8-slim-buster

WORKDIR  /app

COPY . .

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awsliv2.zip" && unzip awscliv2.zip
RUN ./aws/install
RUN pip install -r requirements.txt
