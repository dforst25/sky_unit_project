FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./service-b-cleaning .

CMD ["uvicorn", "main:app", "--port", "=8002", "--host", "=0.0.0.0"]
