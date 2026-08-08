# Реестр подклассов

Реализуйте generic-базовый класс `Handler`. Конкретный обработчик объявляется
как `class JsonHandler(Handler, kind="json")` и автоматически попадает в реестр
через `__init_subclass__`. Метод `Handler.create(kind, *args, **kwargs)` должен
создавать экземпляр зарегистрированного класса. Для неизвестного ключа нужен
`KeyError`, а повторная регистрация того же ключа должна бросать `ValueError` в
момент определения класса. У каждого прямого наследника `Handler` должен быть
собственный реестр, не связанный с реестрами соседних иерархий.

Запуск: `pytest 10_typing_and_metaprogramming/02_subclass_registry`.

## Полезные материалы

- [`object.__init_subclass__`](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__) — настройка класса в момент наследования.
- [`typing.Self`](https://docs.python.org/3/library/typing.html#typing.Self) — тип экземпляра текущего класса.
