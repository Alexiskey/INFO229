FROM python:3.6.3

ENV BIND_PORT 5000
ENV REDIS_HOST localhost
ENV REDIS_PORT 6379

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./main.py /main.py

EXPOSE $BIND_PORT

CMD [ "python", "/main.py" ]
