import pytest


def test_category_iterator(category_iterator):
    assert category_iterator.index == 0
    assert next(category_iterator) == "Iphone 13, 80000.0 руб. Остаток: 1 шт."
    assert next(category_iterator) == "IPhone 16, 120000.0 руб. Остаток: 5 шт."

    with pytest.raises(StopIteration):
        next(category_iterator)
