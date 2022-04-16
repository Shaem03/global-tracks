FROM python:3.8.0-slim

MAINTAINER muhammedshaheem7@gmail.com

RUN apt-get update -y

RUN apt-get install gunicorn3 -y

ADD . /app/

WORKDIR /app/

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers=1", "--timeout=300"]