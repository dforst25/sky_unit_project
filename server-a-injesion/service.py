import requests
import os


SERVICE_B_URL = os.getenv('SERVICE_B_URL', 'http://localhost:8002/clean')

def send_records_to_service_b(records: list[dict]):
    response = requests.post(SERVICE_B_URL, json=records)
    return response.json()