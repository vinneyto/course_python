class Temperature:
    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        raise NotImplementedError

    @celsius.setter
    def celsius(self, value: float) -> None:
        raise NotImplementedError

    @property
    def fahrenheit(self) -> float:
        raise NotImplementedError

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        raise NotImplementedError

    @property
    def kelvin(self) -> float:
        raise NotImplementedError
