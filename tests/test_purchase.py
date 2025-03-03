import random
import pytest
import json
from pages.purchase import PurchaseAPI
from utils.request_handler import load_from_json, save_to_json

PURCHASE_DATA = "purchase_data.json"


@pytest.fixture
def purchase_payload():
    """Test uchun purchase ma'lumotlari"""
    purchase_number = str(random.randint(100000, 9999999999))
    save_to_json(PURCHASE_DATA, {"purchase_number": purchase_number})
    print(f"🔹 purchase_number: {purchase_number}")

    return {
        "purchase": [
            {
                "filial_code": "1212",
                "external_id": "",
                "purchase_id": "",
                "purchase_number": purchase_number,
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
    """Purchase yaratish testi"""
    response = PurchaseAPI.create_purchase(purchase_payload)

    print("✅ API Response:", response.json())

    assert response.status_code == 200, f"❌ Xato! Status kod: {response.status_code}, Response: {response.text}"

    response_data = response.json()
    assert "successes" in response_data and len(response_data["successes"]) > 0, "❌ Purchase yaratilmadi!"

    purchase_number = load_from_json(PURCHASE_DATA)["purchase_number"]
    print(f"✅ Purchase yaratildi. JSON ga saqlangan purchase_number: {purchase_number}")


def test_get_purchases():
    """Barcha purchase larni olish va oldin yaratilgan note bo‘yicha purchase_id va purchase_item_id topish"""
    saved_purchase_number = load_from_json(PURCHASE_DATA)["purchase_number"]
    assert saved_purchase_number is not None, "❌ JSON fayldan purchase_number ni o‘qib olinmadi!"

    response = PurchaseAPI.get_purchases()

    print("✅ API Response:")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))

    assert response.status_code == 200, f"❌ Xato! Status kod: {response.status_code}, Response: {response.text}"

    response_data = response.json()
    assert "purchase" in response_data, "❌ 'purchase' kaliti JSON javobda yo‘q!"
    assert len(response_data["purchase"]) > 0, "❌ 'purchase' ro‘yxati bo‘sh!"

    purchases = response_data["purchase"]

    # API dan kelgan barcha purchase'larni chop etamiz
    print("🔹 API dan qaytgan purchase'lar:")
    for purchase in purchases:
        print(f"   - Purchase ID: {purchase['purchase_id']}, Note: {purchase.get('note')}")

    saved_purchase_id = None
    saved_purchase_item_id = None

    # JSON dagi saqlangan `note` bo‘yicha purchase'ni izlab topamiz
    for purchase in purchases:
        if "purchase_number" in purchase and purchase["purchase_number"] is not None and str(purchase["purchase_number"]) == saved_purchase_number:
            saved_purchase_id = purchase["purchase_id"]
            if "purchase_items" in purchase and len(purchase["purchase_items"]) > 0:
                saved_purchase_item_id = purchase["purchase_items"][0]["purchase_item_id"]
            break

    # Topilgan purchase_id va purchase_item_id JSON ga saqlanadi
    if saved_purchase_id and saved_purchase_item_id:
        save_to_json(PURCHASE_DATA, {
            "purchase_id": saved_purchase_id,
            "purchase_item_id": saved_purchase_item_id
        })
        print(f"✅ Topildi! Purchase ID: {saved_purchase_id}, Purchase Item ID: {saved_purchase_item_id}")

    assert saved_purchase_id is not None, f"❌ Biz yaratgan purchase topilmadi! JSON saqlangan saved_purchase_number: {saved_purchase_number}"
    assert saved_purchase_item_id is not None, f"❌ Purchase ichidan purchase_item_id topilmadi! Purchase ID: {saved_purchase_id}"
