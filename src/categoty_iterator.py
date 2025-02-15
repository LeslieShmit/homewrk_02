from src.category import Category


class CategoryIterator:
    """Класс, принимающий объект класса Category и возвращающий объект, в котором можно будет перебирать циклом
    товары в принятом объекте"""

    category_obj: Category

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        products_list = self.category.products.split("\n")[:-1]
        if self.index < len(products_list):
            result = products_list[self.index]
            self.index += 1
            print(products_list)
            return result
        else:
            raise StopIteration
