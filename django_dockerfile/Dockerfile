FROM python:3.8-slim-bullseye

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install django && \
    pip install gunicorn

WORKDIR /app

ADD Django.tar.gz /app

EXPOSE 8080/tcp

ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:8080 mysite_django.wsgi
