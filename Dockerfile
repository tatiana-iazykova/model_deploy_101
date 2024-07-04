FROM python:3.11.9-slim-bookworm

WORKDIR /app

RUN apt update -y && apt install git build-essential cmake -y

RUN pip3 install -U pip wheel setuptools
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]