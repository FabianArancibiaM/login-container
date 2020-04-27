FROM python:3.7.3-alpine

RUN mkdir -p /app

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip3  install -r requirements.txt

COPY ./src/ /app/
ENV FLASK_APP=app.py

CMD flask run -h 0.0.0.0 -p 5000