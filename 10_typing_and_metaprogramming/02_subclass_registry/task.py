from typing import Any, ClassVar, Self


class Handler:
    """Base class whose named subclasses can be instantiated from a registry."""

    _registry: ClassVar[dict[str, type["Handler"]]]

    def __init_subclass__(cls, *, kind: str | None = None, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if cls.__base__ is Handler:
            cls._registry = {}
        # TODO: зарегистрируйте cls под ключом kind в реестре корня и проверьте дубликаты.

    @classmethod
    def create(cls, kind: str, *args: Any, **kwargs: Any) -> Self:
        # TODO: найдите класс по ключу и передайте ему аргументы конструктора.
        raise NotImplementedError
