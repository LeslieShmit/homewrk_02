def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны - это карманные компьютеры, по сути"
    assert len(category_1.products_list) == 2

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 7
    assert category_2.product_count == 7

def test_category_products_list_property(category_1):
    assert category_1.products == "Iphone 13, 80000.0 руб. Остаток: 1 шт.\nIPhone 16, 120000.0 руб. Остаток: 5 шт.\n"

def test_add_product(category_1, product):
    assert len(category_1.products_list) == 2
    category_1.add_product(product)
    assert len(category_1.products_list) == 3