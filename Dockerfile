FROM python:3.7

COPY ./requirements.txt /src
RUN pip install -r /src/requirements.txt
