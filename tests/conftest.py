import pytest

from src.products import Category, Product


@pytest.fixture
def product() -> Product:
    """
    Тестовые данные для класса Products
    """
    return Product("Имя", "Описание", 1.1, 1)


@pytest.fixture
def product2() -> Product:
    """
    Тестовые данные для класса Category
    """
    return Product("Имя2", "Описание2", 2.2, 2)


@pytest.fixture
def category(product: Product) -> Category:
    """
    Тестовые данные для класса Category
    """
    return Category("Имя", "Описание", [product])


@pytest.fixture
def new_product() -> dict:
    """
    Данные для метода new_product, Product
    """
    return {"name": "Имя", "description": "Описание", "price": 1.0, "quantity": 9}


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0
