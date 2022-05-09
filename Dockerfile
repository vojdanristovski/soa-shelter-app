FROM python:3.8.2-buster
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .