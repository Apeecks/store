from typing import Any

import pytest

from src.products import Category, Product


@pytest.fixture
def products() -> Any:
    """
    Тестовые данные для класса Products
    """
    return Product("Имя", "Описание", 1.1, 1)


@pytest.fixture
def category(products: Product) -> Any:
    return Category("Имя", "Описание", [
        products,
        Product("Имя2", "Описание2", 2.2, 2)
    ])
