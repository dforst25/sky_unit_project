import requests


def send_data_to_service_c(url, data):
    response = requests.post(url, json=data)
    return response.json()