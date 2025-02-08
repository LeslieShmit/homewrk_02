class Product:
    """Класс для представления товара"""
    name: str
    description: str
    price: float
    quantity: int

    # # Атрибут, суммирующий общее количество товаров
    total_quantity = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.total_quantity += self.quantity
