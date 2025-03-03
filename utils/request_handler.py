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
    """JSON faylni yaratish, mavjud bo'lsa ma'lumotni yangilash yoki yangi data qo'shish"""
    existing_data = {}

    # Agar fayl mavjud bo'lsa, avval uni o'qiymiz
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                existing_data = json.load(file)
                if not isinstance(existing_data, dict):  # Agar ma'lumot lug‘at bo'lmasa, uni lug‘atga o‘giramiz
                    existing_data = {}
            except json.JSONDecodeError:
                existing_data = {}

    # Mavjud ma'lumotni yangilash yoki qo'shish
    for key, value in data.items():
        existing_data[key] = value  # Kalit bo'yicha eski ma'lumotni yangilash yoki yangi ma'lumot qo'shish

    # Yangilangan ma'lumotni faylga yozamiz
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=4)



def load_from_json(file_path):
    """Berilgan JSON fayldan ma'lumotni yuklash"""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return None
