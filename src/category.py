class Category:
    """Класс для представления категории"""

    name: str
    description: str
    products: list

    # Атрибут, показывающий количество категорий
    category_count = 0

    # Атрибут, показывающий количество товаров
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1

        for product in self.products:
            Category.product_count += product.quantity
