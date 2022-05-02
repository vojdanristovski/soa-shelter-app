FROM python:3.8.2-buster
WORKDIR /app
COPY app/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY app .
CMD [ "python", "/src/main.py" ]