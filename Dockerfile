FROM python:3.9.0
WORKDIR /app
RUN apt-get -y update
RUN apt-get -y install vim
COPY requirements.txt /requirements.txt
RUN pip install --trusted-host pypi.python.org -r /requirements.txt
COPY ./ /app/

