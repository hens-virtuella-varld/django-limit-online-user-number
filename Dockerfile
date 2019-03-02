FROM python:3.7

RUN mkdir /src
COPY ./requirements.txt /src/
RUN pip install -r /src/requirements.txt
