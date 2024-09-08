FROM python:3.11.4

WORKDIR /app

COPY requirements.txt . 

RUN pip install requests

COPY . . 

CMD ["python", "./main.py"]

