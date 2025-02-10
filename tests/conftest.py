import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(name="Iphone 13", description="Iphone 13 - ни дать, ни взять", price=80000.0, quantity=1)


@pytest.fixture
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны - это карманные компьютеры, по сути",
        products=[
            Product(name="Iphone 13", description="Iphone 13 - ни дать, ни взять", price=80000.0, quantity=1),
            Product(name="IPhone 16", description="Последняя модель IPhone", price=120000.0, quantity=5),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Планшеты",
        description="Планшеты - то же, что и смартфон, только больше",
        products=[Product(name="Ipad Pro", description="Последняя модель Ipad", price=150000.0, quantity=1)],
    )

@pytest.fixture
def product_dict():
    return {"name": "Iphone 13", "description": "Iphone 13 - ни дать, ни взять", "price": 80000.0, "quantity": 1}

@pytest.fixture
def list_of_products():
    return [
            Product(name="Iphone 13", description="Iphone 13 - ни дать, ни взять", price=70000.0, quantity=1),
            Product(name="IPhone 16", description="Последняя модель IPhone", price=120000.0, quantity=5),
        ]

@pytest.fixture
def list_of_products_2():
    return [Product(name="Ipad Pro", description="Последняя модель Ipad", price=150000.0, quantity=1)]