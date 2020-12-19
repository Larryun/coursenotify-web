#FROM tiangolo/meinheld-gunicorn-flask:python3.7
FROM python:3.6.8

RUN mkdir /app
RUN mkdir /app/data
RUN mkdir /app/instance
COPY ./coursenotify /app/coursenotify/
COPY ./instance /app/instance/
WORKDIR /app

#RUN pip install -e "git+https://github.com/Larryun/coursenotify_v2#egg=cn_v2"
RUN pip install -r coursenotify/requirements.txt
