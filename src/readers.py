import json

from src.category import Category
from src.product import Product


def json_reader(path_to_file: str) -> list[dict]:
    """Функция считывает json-file и преобразовывает его в лист словарей"""
    with open(path_to_file, encoding="utf-8") as f:
        data = json.load(f)
        return data


def create_object_from_json(data: list[dict]) -> list:
    """Функция принимает лист словарей, преобразованный из json-файла и возвращает список из экземпляров класса"""
    categories = []
    for category_dict in data:
        products = []
        for product_dict in category_dict["products"]:
            products.append(Product(**product_dict))
        category_dict["products"] = products
        categories.append(Category(**category_dict))
    return categories
