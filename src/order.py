from src.abstract_group import AbstractGroup
from src.product import Product


class Order(AbstractGroup):
    product: Product
    quantity: int
    total_price: float

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        return f"Заказанный товар: {self.product.name}, кол-во: {self.quantity}, общая стоимость: {self.total_price}"
