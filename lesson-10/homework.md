# Домашнее задание #10 (Расширения на C)

### 1. Реализовать библиотеку для парсинга и сериализации json (с помощью C API)
- Нужно написать модуль custom_json, который имел бы хотя бы два метода: loads и dumps;
- Методу loads на вход подаётся строка в формате JSON. Ограничения:
    * JSON-сообщение в виде набор пар ключ-значение (читай как python-словарь);
    * Ключём в JSON **всегда** является строка в двойных кавычках;
    * Значением может выступать либо число, либо строка. Если захотелось приключений, то можно сделать поддержку и других типов;
    * Если входная строка не является JSON-объектом, то выбрасывается исключение
       ```C
       ...
       PyErr_Format(PyExc_TypeError, "Expected object or value");
       return NULL;
       ```
    * Возвращаться должен объект типа dict. Например, можно сделать так:
        ```C
        PyObject *dict = NULL;
        if (!(dict = PyDict_New())) {
            printf("ERROR: Failed to create Dict Object\n");
            return NULL;
        }

        PyObject *key = NULL;
        PyObject *value = NULL;

        if (!(key = Py_BuildValue("s", "hello"))) {
            printf("ERROR: Failed to build string value\n");
            return NULL;
        }
        if (!(value = Py_BuildValue("i", 10))) {
            printf("ERROR: Failed to build integer value\n");
            return NULL;
        }
        if (PyDict_SetItem(dict, key, value) < 0) {
            printf("ERROR: Failed to set item\n");
            return NULL;
        }
        if (!(key = Py_BuildValue("s", "world"))) {
            printf("ERROR: Failed to build string value\n");
            return NULL;
        }
        if (!(value = Py_BuildValue("s", "100500"))) {
            printf("ERROR: Failed to build string value\n");
            return NULL;
        }
        if (PyDict_SetItem(dict, key, value) < 0) {
            printf("ERROR: Failed to set item\n");
            return NULL;
        }

        return dict;
        ```
- Методу dumps в качестве аргумента передаётся объект типа dict и возвращает строку. Ограничения как у loads только наоборот;

Готовое расширение используется из Python:
```Python
import json

import custom_json


def main():
    json_str = '{"hello": 10, "world": "value"}'

    json_doc = json.loads(json_str)
    cust_json_doc = custom_json.loads(json_str)

    assert json_doc == cust_json_doc
    assert json_str == cust_json.dumps(cust_json.loads(json_str))


if __name__ == "__main__":
    main()
```

### 2. Тесты корректности на уровне Python в отдельном модуле

### 3. Тесты производительности
Сравнивать скорость работы своей реализации с json на одних и тех же данных.
Данные должны быть большие (как количество JSON, так и размер каждого JSON). Требование: выполнение тестов не менее 100 мс.

Для генерации тестовых JSON можно использовать статический найденный на просторах интернета JSON.
Можно попробовать использовать библиотеку [Faker](https://faker.readthedocs.io/en/master/) для генерации данных.
Допустимо генерировать рандомные данные.

### 4. Зеленый пайплайн в репе
