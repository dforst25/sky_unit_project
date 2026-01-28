FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./server-a-injesion .

CMD ["uvicorn", "main:app", "--port", "=8001", "--host", "=0.0.0.0"]
