from typing import Any

from src.products import Category


def test_class_prod_cat(products: Any, category: Any) -> Any:
    """
    Тест классов в модуле products
    """
    assert products.name == "Имя"
    assert products.description == "Описание"
    assert products.price == 1.1
    assert products.quantity == 1

    assert category.name == "Имя"
    assert category.description == "Описание"
    assert Category.category_count == 1
    assert Category.product_count == 2

    Category("Еще категория", "Описание", [products])
    assert Category.category_count == 2
    assert Category.product_count == 3
