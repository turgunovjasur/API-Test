import json
import os
import requests
from requests.auth import HTTPBasicAuth
from utils.config import USERNAME, PASSWORD, HEADERS


def send_request(method, url, payload=None):
    """
    API so‘rovlarini yuborish.
    method: "GET", "POST", "PUT", "DELETE"
    url: API endpoint
    payload: JSON ma'lumot (faqat POST yoki PUT uchun)
    """
    auth = HTTPBasicAuth(USERNAME, PASSWORD)
    response = requests.request(method, url, json=payload, headers=HEADERS, auth=auth)
    return response


def save_to_json(file_path, data):
    """Berilgan ma'lumotni JSON faylga saqlash"""
    with open(file_path, "w") as file:
        json.dump(data, file)


def load_from_json(file_path):
    """Berilgan JSON fayldan ma'lumotni yuklash"""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return None
