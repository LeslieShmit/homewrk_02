import pytest

from src.category import Category
from src.categoty_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.order import Order
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product():
    return Product(name="Iphone 13", description="Iphone 13 - ни дать, ни взять", price=80000.0, quantity=1)


@pytest.fixture
def product_2():
    return Product(name="IPhone 16", description="Последняя модель IPhone", price=120000.0, quantity=5)


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


@pytest.fixture
def category_iterator(category_1):
    return CategoryIterator(category_1)


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Германия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "Италия", "5 дней", "Темно-зеленый")


@pytest.fixture
def order():
    return Order(Product(name="Iphone 13", description="Iphone 13 - ни дать, ни взять", price=80000.0, quantity=1), 2)


@pytest.fixture
def empty_category():
    return Category("Пустая категория", "Категория без продуктов", [])
