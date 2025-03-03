import pytest
import json
from pages.input import InputAPI
from tests.test_purchase import PURCHASE_DATA
from utils.request_handler import load_from_json


@pytest.fixture
def input_payload():
    """Test uchun input ma'lumotlari"""
    purchase_data = load_from_json(PURCHASE_DATA)
    assert purchase_data is not None, "❌ JSON fayldan purchase ma'lumotlari o‘qib olinmadi!"
    assert "purchase_id" in purchase_data and "purchase_item_id" in purchase_data, "❌ JSON ichida purchase_id yoki purchase_item_id mavjud emas!"

    purchase_id = purchase_data["purchase_id"]
    purchase_item_id = purchase_data["purchase_item_id"]

    print(f"🔹 Yuklangan purchase_id: {purchase_id}, purchase_item_id: {purchase_item_id}")

    return {
        "input": [
            {
                "filial_code": "1212",
                "external_id": "",
                "input_id": "",
                "input_number": "",
                "input_time": "03.03.2025",
                "status": "N",
                "warehouse_code": "0106",
                "note": "test api-1",
                "input_items": [
                    {
                        "external_id": None,
                        "input_item_id": "",
                        "purchase_id": purchase_id,
                        "purchase_item_id": purchase_item_id,
                        "product_code": "4545",
                        "inventory_kind": "G",
                        "card_code": None,
                        "expiry_date": None,
                        "quantity": "10",
                        "price": "10000",
                        "margin_kind": "P",
                        "margin_value": "0",
                        "vat_percent": None,
                        "vat_amount": "0"
                    }
                ]
            }
        ]
    }


def test_create_input(input_payload):
    """Input yaratish testi"""
    response = InputAPI.create_input(input_payload)

    print("✅ API Response:", response.json())

    assert response.status_code == 200, f"❌ Xato! Status kod: {response.status_code}, Response: {response.text}"

    response_data = response.json()

    assert "successes" in response_data and len(response_data["successes"]) > 0, "❌ Input yaratilmadi!"


def test_get_inputs():
    """Barcha input larni olish va natijani tekshirish"""
    response = InputAPI.get_inputs()

    response_data = response.json()

    print("✅ API Response:")
    print(json.dumps(response_data, indent=4, ensure_ascii=False))

    assert response.status_code == 200, f"❌ Xato! Status kod: {response.status_code}, Response: {response.text}"

    assert "input" in response_data, "❌ 'input' kaliti JSON javobda yo‘q!"

    assert len(response_data["input"]) > 0, "❌ 'input' ro‘yxati bo‘sh!"
