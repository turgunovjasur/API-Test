from utils.request_handler import send_request
from utils.config import ENDPOINTS


class PurchaseAPI:
    """Purchase API uchun Page Object"""

    @staticmethod
    def create_purchase(payload):
        """Purchase yaratish"""
        response = send_request("POST", ENDPOINTS["purchase_import"], payload)
        return response

    @staticmethod
    def get_purchases():
        """Purchase ro‘yxatini olish"""
        response = send_request("GET", ENDPOINTS["purchase_export"])
        return response
