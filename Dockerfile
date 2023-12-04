FROM python:3.10.12

ENV PYTHONUNBUFFERED 1

WORKDIR /mqhandler
RUN python -m pip install --upgrade pip

COPY . ./

RUN pip install -e .
