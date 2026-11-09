import pytest

from src.lawn_grass import LawnGrass
from src.products import Category, Product
from src.smartphone import Smartphone


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


@pytest.fixture
def prod1_smartphone() -> Smartphone:
    return Smartphone(
        "Phone1", "Описание1", 1.0, 1,
        1.0, "1", 1, "Цвет1"
    )


@pytest.fixture
def prod2_smartphone() -> Smartphone:
    return Smartphone(
        "Phone2", "Описание2", 2.0, 2,
        2.0, "2", 2, "Цвет2"
    )


@pytest.fixture
def prod1_grass() -> LawnGrass:
    return LawnGrass(
        "Трава1", "Описание1", 1.0, 1,
        "Страна1", "1 день", "Цвет1"
    )


@pytest.fixture
def prod2_grass() -> LawnGrass:
    return LawnGrass(
        "Трава2", "Описание2", 2.0, 2,
        "Страна2", "2 дня", "Цвет2"
    )
