FROM python:3.11

ADD . /src
WORKDIR /src
RUN apt-get update
RUN pip3 install -r /src/requirements.txt
ENV PYTHONPATH /src
EXPOSE  8080