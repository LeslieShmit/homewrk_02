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
        self.__products = products

        Category.category_count += 1

        for product in self.__products:
            Category.product_count += product.quantity


    def add_product(self, product_obj):
        self.__products.append(product_obj)
        Category.product_count += product_obj.quantity

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def products_list(self):
        return self.__products
