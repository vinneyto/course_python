# Полиморфные уведомления

Опишите абстрактный класс `Notification` с абстрактным методом `render()`.
Реализуйте классы `EmailNotification(recipient, subject, body)` и
`SmsNotification(phone, text)`. Их `render()` возвращает соответственно строки
`"To: <recipient> | <subject> | <body>"` и `"SMS <phone>: <text>"`.

Функция `render_all` принимает итерируемый объект уведомлений и возвращает
список результатов, работая только через общий интерфейс `Notification`.
Создать экземпляр базового класса напрямую быть не должно быть возможно.

## Полезные материалы

- [`abc`](https://docs.python.org/3/library/abc.html) — абстрактные базовые классы и `abstractmethod`.
- [Наследование](https://docs.python.org/3/tutorial/classes.html#inheritance) — переопределение методов и полиморфизм.
