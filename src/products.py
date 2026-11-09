from typing import Any

from src.base_product import BaseProduct
from src.mixin_repr import MixinRepr


class Product(MixinRepr, BaseProduct):
    __price: float

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.__price = price
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного класса")

        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, prod_dict: Any, prods_list: list | None = None) -> Any:
        """
        Принимает словарь данных Product и список продуктов.
        Добавляет или складывает похожие объекты
        """
        new_prod = cls(
            prod_dict.get("name"), prod_dict.get("description"),
            prod_dict.get("price"), prod_dict.get("quantity")
        )
        for prod in prods_list or []:
            if new_prod.name == prod.name:
                new_prod.quantity = new_prod.quantity + prod.quantity
                if new_prod.__price != prod.__price:
                    if new_prod.__price < prod.__price:
                        new_prod.__price = prod.__price
        return new_prod

    @property
    def price(self) -> float:
        """
        Возвращает приватную цену продукта
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        self.__price = new_price


class Category:
    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, prod: Product) -> Any:
        """
        Добавляет продукт в приватный список продуктов
        """
        if not isinstance(prod, Product):
            raise TypeError("Можно добавить только объект Product")

        self.__products.append(prod)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Выводит продукты в приватном списке, формат: str
        """
        product_str = ""
        for x in self.__products:
            product_str += f"{x.name}, {x.price} руб. Остаток: {x.quantity} шт.\n"
        return product_str

    def middle_price(self) -> float:
        """
        Возвращает среднюю цену товаров категории.
        """
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0
