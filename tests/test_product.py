from src.product import Product


def test_product_init(product):
    assert product.name == "Iphone 13"
    assert product.description == "Iphone 13 - ни дать, ни взять"
    assert product.price == 80000.0
    assert product.quantity == 1


def test_new_product_no_list_of_products(product_dict):
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Iphone 13"
    assert new_product.description == "Iphone 13 - ни дать, ни взять"
    assert new_product.price == 80000.0
    assert new_product.quantity == 1


def test_new_product_existing_product(product_dict, list_of_products):
    new_product = Product.new_product(product_dict, list_of_products)
    assert new_product.name == "Iphone 13"
    assert new_product.description == "Iphone 13 - ни дать, ни взять"
    assert new_product.price == 80000.0
    assert new_product.quantity == 2


def test_new_product_non_existing_product(product_dict, list_of_products_2):
    new_product = Product.new_product(product_dict, list_of_products_2)
    assert new_product.name == "Iphone 13"
    assert new_product.description == "Iphone 13 - ни дать, ни взять"
    assert new_product.price == 80000.0
    assert new_product.quantity == 1


def test_price_property(product):
    assert product.price == 80000.0


def test_price_setter(product):
    product.price = 100000
    assert product.price == 100000
