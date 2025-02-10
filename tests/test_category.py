def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны - это карманные компьютеры, по сути"
    assert len(category_1.products_list) == 2

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 7
    assert category_2.product_count == 7
