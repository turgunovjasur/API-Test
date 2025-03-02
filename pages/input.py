from utils.request_handler import send_request
from utils.config import ENDPOINTS


class InputAPI:
    """Input API uchun Page Object"""

    @staticmethod
    def create_input(payload):
        """Input yaratish"""
        response = send_request("POST", ENDPOINTS["input_import"], payload)
        return response

    @staticmethod
    def get_inputs():
        """Input ro‘yxatini olish"""
        response = send_request("GET", ENDPOINTS["input_export"])
        return response