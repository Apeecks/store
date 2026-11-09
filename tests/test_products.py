from typing import Any

import pytest

from src.base_product import BaseProduct
from src.lawn_grass import LawnGrass
from src.mixin_repr import MixinRepr
from src.products import Category, Product
from src.smartphone import Smartphone


def test_class_prod_cat(product: Any, category: Any) -> Any:
    """
    Тест классов в модуле products
    """
    assert product.name == "Имя"
    assert product.description == "Описание"
    assert product.price == 1.1
    assert product.quantity == 1

    assert category.name == "Имя"
    assert category.description == "Описание"
    assert Category.category_count == 1
    assert Category.product_count == 1

    Category("Еще категория", "Описание", [product])
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_product_new_funcs(capsys: Any, product: Product, new_product: dict) -> Any:
    """
    Тесты новой функциональности, hw14_2, class Product
    """
    prod_assert = Product("Имя", "Описание", 1.1, 10)
    new_prod = Product.new_product(new_product, [product])

    assert new_prod.name == prod_assert.name
    assert new_prod.description == prod_assert.description
    assert new_prod.price == prod_assert.price
    assert new_prod.quantity == prod_assert.quantity

    capsys.readouterr()

    product.price = -100
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"

    assert product.price == 1.1

    product.price = 1.0
    assert product.price == 1.0

    product.price = 0
    assert product.price == 1.0


def test_category_new_funcs(capsys: Any, category: Category, product2: Product) -> Any:
    """
    Тесты новой функциональности, hw14_2, class Category
    """
    assert Category.product_count == 1

    capsys.readouterr()

    print(category.products)
    captured = capsys.readouterr()
    assert captured.out == "Имя, 1.1 руб. Остаток: 1 шт.\n\n"

    category.add_product(product2)

    assert Category.product_count == 2

    print(category.products)
    captured = capsys.readouterr()
    assert captured.out == (
        f"Имя, 1.1 руб. Остаток: 1 шт.\n"
        f"{product2.name}, 2.2 руб. Остаток: 2 шт.\n\n"
    )


def test_magic_methods(product: Product, product2: Product, category: Category) -> None:
    assert str(product) == "Имя, 1.1 руб. Остаток: 1 шт."

    assert product + product2 == 5.5

    category.add_product(product2)
    assert str(category) == "Имя, количество продуктов: 3 шт."


def test_smartphone(
    prod1_smartphone: Smartphone,
    prod2_smartphone: Smartphone
) -> None:
    assert isinstance(prod1_smartphone, Product)

    assert prod1_smartphone.name == "Phone1"
    assert prod1_smartphone.description == "Описание1"
    assert prod1_smartphone.price == 1.0
    assert prod1_smartphone.quantity == 1

    assert prod1_smartphone.efficiency == 1.0
    assert prod1_smartphone.model == "1"
    assert prod1_smartphone.memory == 1
    assert prod1_smartphone.color == "Цвет1"

    assert prod1_smartphone + prod2_smartphone == 5.0


def test_lawn_grass(
    prod1_grass: LawnGrass,
    prod2_grass: LawnGrass
) -> None:
    assert isinstance(prod1_grass, Product)

    assert prod1_grass.name == "Трава1"
    assert prod1_grass.description == "Описание1"
    assert prod1_grass.price == 1.0
    assert prod1_grass.quantity == 1

    assert prod1_grass.country == "Страна1"
    assert prod1_grass.germination_period == "1 день"
    assert prod1_grass.color == "Цвет1"

    assert prod1_grass + prod2_grass == 5.0


def test_type_restrictions(
    category: Category,
    product: Product,
    prod1_smartphone: Smartphone,
    prod1_grass: LawnGrass
) -> None:

    with pytest.raises(TypeError):
        prod1_smartphone + prod1_grass

    with pytest.raises(TypeError):
        prod1_grass + prod1_smartphone

    with pytest.raises(TypeError):
        product + prod1_smartphone

    category.add_product(prod1_smartphone)
    category.add_product(prod1_grass)

    assert Category.product_count == 3

    invalid_product: Any = "Not a product"

    with pytest.raises(TypeError):
        category.add_product(invalid_product)

    assert Category.product_count == 3


def test_abstract_product() -> None:
    with pytest.raises(TypeError):
        BaseProduct("Товар", "Описание", 100, 1)

    assert issubclass(Product, BaseProduct)
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)

    assert Smartphone.__bases__ == (Product,)
    assert LawnGrass.__bases__ == (Product,)

    assert issubclass(Product, MixinRepr)


def test_mixin_repr(capsys: Any) -> None:
    product = Product("Продукт1", "Описание продукта", 1200, 10)

    captured = capsys.readouterr()

    assert captured.out == "Product('Продукт1', 'Описание продукта', 1200, 10)\n"

    assert repr(product) == "Product('Продукт1', 'Описание продукта', 1200, 10)"

    smartphone = Smartphone(
        "Телефон", "Описание", 2000, 2,
        95.5, "A1", 128, "Чёрный"
    )

    grass = LawnGrass(
        "Трава", "Описание", 100, 3,
        "Россия", "7 дней", "Зелёный"
    )

    captured = capsys.readouterr()

    assert captured.out == (
        "Smartphone('Телефон', 'Описание', 2000, 2)\n"
        "LawnGrass('Трава', 'Описание', 100, 3)\n"
    )

    assert smartphone.price == 2000
    assert grass.quantity == 3


def test_zero_quantity_product() -> None:
    with pytest.raises(ValueError, match="^Товар с нулевым количеством не может быть добавлен$"):
        Product("Бракованный товар", "Описание", 1000.0, 0)

    with pytest.raises(ValueError, match="^Товар с нулевым количеством не может быть добавлен$"):
        Smartphone("Телефон", "Описание", 2000.0, 0, 95.5, "A1", 128, "Чёрный")

    with pytest.raises(ValueError, match="^Товар с нулевым количеством не может быть добавлен$"):
        LawnGrass("Трава", "Описание", 100.0, 0, "Россия", "7 дней", "Зелёный")


def test_middle_price(product: Product, product2: Product) -> None:
    category = Category("Товары", "Описание", [product, product2])
    assert category.middle_price() == pytest.approx(1.65)

    category.add_product(Product("Товар3", "Описание", 4.7, 100))
    assert category.middle_price() == pytest.approx((1.1 + 2.2 + 4.7) / 3)

    empty_category = Category("Пустая категория", "Описание", [])
    assert empty_category.middle_price() == 0
