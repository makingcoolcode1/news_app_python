
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y python3-requests

COPY . . 

CMD ["python3", "main.py"]