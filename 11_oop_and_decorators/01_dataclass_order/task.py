from dataclasses import dataclass


@dataclass(frozen=True, order=True, slots=True)
class OrderLine:
    name: str
    unit_price: float
    quantity: int = 1

    def __post_init__(self) -> None:
        # TODO: проверьте инварианты объекта.
        raise NotImplementedError

    @property
    def total(self) -> float:
        raise NotImplementedError
