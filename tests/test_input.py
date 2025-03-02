import pytest
import json
from pages.input import InputAPI


@pytest.fixture
def input_payload():
    """Test uchun input ma'lumotlari"""
    return {
      "filial_codes": [
        {
          "filial_code": ""
        }
      ],
      "filial_code": "",
      "external_id": "",
      "input_id": "1157959",  # STATIC DATA
      "begin_input_date": "",
      "end_input_date": "",
      "begin_created_on": "",
      "end_created_on": "",
      "begin_modified_on": "",
      "end_modified_on": ""
    }


def test_create_input(purchase_payload):
    """✅ Input yaratish test"""
    response = InputAPI.create_input(purchase_payload)

    print("✅ API Response:", response.json())

    assert response.status_code == 200, f"❌ Xato! Status kod: {response.status_code}, Response: {response.text}"

    response_data = response.json()

    assert "successes" in response_data and len(response_data["successes"]) > 0, "❌ Input yaratilmadi!"


def test_get_inputs():
    """✅ Barcha input larni olish va natijani tekshirish"""
    response = InputAPI.get_inputs()

    response_data = response.json()

    print("✅ API Response:")
    print(json.dumps(response_data, indent=4, ensure_ascii=False))

    assert response.status_code == 200, f"❌ Xato! Status kod: {response.status_code}, Response: {response.text}"

    assert "input" in response_data, "❌ 'input' kaliti JSON javobda yo‘q!"

    assert len(response_data["input"]) > 0, "❌ 'input' ro‘yxati bo‘sh!"




