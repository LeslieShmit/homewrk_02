import pytest

from src.product import Product
def test_product_init(product):
    assert product.name == "Iphone 13"
    assert product.description == "Iphone 13 - ни дать, ни взять"
    assert product.price == 80000.0
    assert product.quantity == 1
