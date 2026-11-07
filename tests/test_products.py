from typing import Any

from src.products import Category, Product


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
