import requests


def send_data_to_service_c(url, data):
    response = requests.post(f'http://{url}:8003/records', json=data)
    return response.json()