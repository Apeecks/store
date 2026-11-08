from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, prod_dict: Any, prods_list: list | None = None) -> Any:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass
