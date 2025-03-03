import pytest


def test_all():
    pytest.main([
        # Purchase
        "-v",
        "tests/test_purchase.py::test_create_purchase",
        "tests/test_purchase.py::test_get_purchases",

        # Input
        "tests/test_input.py::test_create_input"])
