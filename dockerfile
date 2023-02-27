#FROM python:3.8-slim-buster
#
#WORKDIR  /app
#
#COPY . .
#
#RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awsliv2.zip" && unzip awscliv2.zip
#RUN ./aws/install
#RUN pip install -r requirements.txt
#
#CMD ["python", "-n" "flask" "run" "--host=0.0.0.0"]

FROM jenkins/jenkins:latest
USER root
RUN apt update && apt-get install zip -y && apt-get install curl -y

#RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip
#RUN ./aws/install

RUN curl -sSL https://get.docker.com/ | sh
USER jenkins