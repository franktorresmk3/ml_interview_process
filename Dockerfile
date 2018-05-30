#FROM python:3.6.5-alpine3.7

## Create app directory
#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app

## Bundle app source
#COPY . /usr/src/app

#RUN pip install --trusted-host pypi.python.org -r requirements.txt

#ENTRYPOINT [ "python", "project" ]



FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt
ADD . /usr/src/app
WORKDIR /usr/src/app/project
ENTRYPOINT [ "python", "__main__.py" ]