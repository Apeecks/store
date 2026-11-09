from typing import Any


class MixinRepr:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, {self.price!r}, {self.quantity!r})"
        )
