import pytest
import json
from pages.purchase import PurchaseAPI


@pytest.fixture
def purchase_payload():
    """Test uchun purchase ma'lumotlari"""
    return {
        "purchase": [
            {
                "filial_code": "1212",
                "external_id": "",
                "purchase_id": "",
                "purchase_number": "",
                "purchase_time": "02.03.2025",
                "order_id": "",
                "status_code": "complete",
                "input_date": "",
                "supplier_code": "postavshik",
                "contract_code": "",
                "warehouse_code": "",
                "currency_code": "860",
                "invoice_number": "",
                "invoice_date": "",
                "total_margin_kind": "",
                "total_margin_value": "",
                "note": "",
                "posted": "Y",
                "purchase_items": [
                    {
                        "external_id": None,
                        "purchase_item_id": "",
                        "order_item_id": None,
                        "product_code": "4545",
                        "inventory_kind": "G",
                        "on_balance": "Y",
                        "serial_number": None,
                        "card_code": None,
                        "expiry_date": None,
                        "base_price": None,
                        "quantity": "10",
                        "price": "10000",
                        "margin_kind": "P",
                        "margin_value": "0",
                        "vat_percent": None,
                        "vat_amount": "0",
                        "marking_codes": []
                    }
                ]
            }
        ]
    }


def test_create_purchase(purchase_payload):
    """✅ Purchase yaratish test"""
    response = PurchaseAPI.create_purchase(purchase_payload)

    print("✅ API Response:", response.json())

    assert response.status_code == 200, f"❌ Xato! Status kod: {response.status_code}, Response: {response.text}"

    response_data = response.json()

    assert "successes" in response_data and len(response_data["successes"]) > 0, "❌ Purchase yaratilmadi!"


def test_get_purchases():
    """✅ Barcha purchase larni olish va natijani tekshirish"""
    response = PurchaseAPI.get_purchases()

    response_data = response.json()

    print("✅ API Response:")
    print(json.dumps(response_data, indent=4, ensure_ascii=False))

    assert response.status_code == 200, f"❌ Xato! Status kod: {response.status_code}, Response: {response.text}"

    assert "purchase" in response_data, "❌ 'purchase' kaliti JSON javobda yo‘q!"

    assert len(response_data["purchase"]) > 0, "❌ 'purchase' ro‘yxati bo‘sh!"




