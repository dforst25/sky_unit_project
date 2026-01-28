FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./service-c-database .

CMD ["uvicorn", "main:app", "--port", "=8003", "--host", "=0.0.0.0"]