from python:3
WORKDIR /code
COPY requirements.txt /code/

run pip install -r requirements.txt

COPY . /code/
