from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product(name="Iphone 13", description="Iphone 13 - ни дать, ни взять", price=80000.0, quantity=1)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Iphone 13', 'Iphone 13 - ни дать, ни взять', 80000.0, 1)"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert (
        message.out.strip() == "Smartphone('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"
    )

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Германия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)"
