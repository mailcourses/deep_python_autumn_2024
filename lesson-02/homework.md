# Домашнее задание #02 (функции)

### 1. Функция для обработки json
Функция для обработки должна принимать параметры:
- строку с json;
- список ключей, которые необходимо обработать;
- список токенов, которые нужно найти;
- функцию-обработчик ключа и токена.

json для задания всегда имеет вид словаря с ключами и значениями из строк.

Функция парсит строку с json библиотечными средствами.
Для каждого ключа json, который совпадает с одним из переданных ключей для обработки, функция должна искать вхождения токенов в строку-значение по данному ключу.
Для каждого найденного токена должна быть вызвана функция-обработчик с ключом и токеном.

Поиск ключей должен зависеть от регистра, а поиск токенов должен быть регистронезависимым.


```py
def process_json(
    json_str: str,
    required_keys: list[str] | None = None,
    tokens: list[str] | None = None,
    callback: Callable[[str, str], None] | None = None,
) -> None:
    ...


# например:
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_keys = ["key1", "KEY2"]
tokens = ["WORD1", "word2"]

process_json(json_str, required_keys, tokens, lambda key, token: f"{key=}, {token=}")

# выведет:
# key="key1", token="WORD1"
# key="key1", token="word2"
```

### 2. Параметризуемый декоратор для логирования вызовов и перезапуска функций в случае ошибок
Декоратор `retry_deco` должен:
- принимать опциональными параметрами число перезапусков декорируемой функции и список ожидаемых классов исключений;
- при вызове функции логировать (выводить) название функции, все переданные ей аргументы, номер попытки перезапуска, результат работы функции и ошибку, если было выброшено исключение;
  формат логирования произвольный (например, функция и аргументы один раз, а номер попытки и исключение/результат сколько потребуется);
- в случае исключения при выполнении функции декоратор должен выполнить новую попытку запуска функции, пока не достигнет заданного числа перезапусков;
  если исключение из списка ожидаемых классов исключений (параметр декоратора), то перезапускать функцию не надо, тк исключения из списка это нормальный режим работы декорируемой функции.

```py
def retry_deco(...):
    ...


@retry_deco(3)
def add(a, b):
    return a + b


add(4, 2)
# run "add" with positional args = (4, 2), attempt = 1, result = 6

add(4, b=3)
# run "add" with positional args = (4,), keyword kwargs = {"b": 3}, attempt = 1, result = 7


@retry_deco(3)
def check_str(value=None):
    if value is None:
        raise ValueError()

    return isinstance(value, str)


check_str(value="123")
# run "check_str" with keyword kwargs = {"value": "123"}, attempt = 1, result = True

check_str(value=1)
# run "check_str" with keyword kwargs = {"value": 1}, attempt = 1, result = False

check_str(value=None)
# run "check_str" with keyword kwargs = {"value": None}, attempt = 1, exception = ValueError
# run "check_str" with keyword kwargs = {"value": None}, attempt = 2, exception = ValueError
# run "check_str" with keyword kwargs = {"value": None}, attempt = 3, exception = ValueError


@retry_deco(2, [ValueError])
def check_int(value=None):
    if value is None:
        raise ValueError()

    return isinstance(value, int)

check_int(value=1)
# run "check_int" with keyword kwargs = {"value": 1}, attempt = 1, result = True

check_int(value=None)
# run "check_int" with keyword kwargs = {"value": None}, attempt = 1, exception = ValueError # нет перезапуска

```

### 3. Тесты в отдельном модуле для каждого пункта

### 4. Перед отправкой на проверку код должен быть прогнан через flake8 и pylint, по желанию еще black

### 5. Покрытие тестов через coverage

### 6. Зеленый пайплайн в репе
