

def test_order_init(order):
    assert order.quantity == 2
    assert order.total_price == 160000.0

def test_order_str(order):
    assert str(order) == "Заказанный товар: Iphone 13, кол-во: 2, общая стоимость: 160000.0"