import requests
import os


SERVICE_B_URL = os.getenv('SERVICE_B_URL', 'localhost')

def send_records_to_service_b(records: list[dict]):
    response = requests.post(f'http://{SERVICE_B_URL}:8002/clean', json=records)
    return response.json()