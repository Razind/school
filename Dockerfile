FROM python:3.11

WORKDIR /app

ADD . /app

RUN apt-get update && apt-get install gcc -y

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]