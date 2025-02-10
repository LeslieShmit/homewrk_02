
class Product:
    """Класс для представления товара"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product_dict, existing_products=None):
        if existing_products:
            for product in existing_products:
                if product.name == new_product_dict["name"]:
                    product.quantity = product.quantity + new_product_dict["quantity"]
                    if new_product_dict["price"] > product.__price:
                        product.__price = new_product_dict["price"]
                    return product
                else:
                    return cls(**new_product_dict)
        else:
            return cls(**new_product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                user_input = input("Введенная стоимость ниже оригинальной. Вы уверены, что хотите продолжить? y/n").lower()
                if user_input == "y":
                    self.__price = new_price
                else:
                    return
            else:
                self.__price = new_price


