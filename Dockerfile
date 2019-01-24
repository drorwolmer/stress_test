FROM python:3.6.6-stretch

RUN pip install gunicorn flask flask-apispec

COPY *.py /tmp/

WORKDIR /tmp/

ENV WORKERS=3

CMD gunicorn -b 0.0.0.0:1234 -w $WORKERS server:app --max-requests 2000 --log-level DEBUG