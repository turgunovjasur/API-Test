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
