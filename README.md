# Банковский виджет

## Описание:

Проект выполняет следующие функции:

- фильтрует список словарей по статусу и сортирует
его по дате;
- маскирует номер карты или счета по заданному правилу;
- форматирует дату в соответствии с заданным правилом;
- фильтрует транзакции по заданной валюте;
- из списка транзакций выводит описание каждой операции по очереди;
- генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
- содержит тесты, проверяющие каждый из модулей на соответствие условиям задачи.

## Требования к окружению:

Установите python 3.13.0

Установите Poetry

Установите Pytest

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/Bugrova-Irina/homework10.1/
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
```
poetry add --group dev pytest
```
## Использование:
Для получения замаскированного счета или номера карты введите номер карты в формате "Visa Platinum 7000792289606361" или номер счета в формате "Счет 73654108430135874305"

Для сортировки словарей задайте список словарей и запустите приложение.

Для получения форматированной даты введите исходные данные в формате 
"2024-03-11T02:26:18.671407"

Для получения списка транзакций, отфильтрованных по заданной валюте, введите список словарей, содержащих транзакции и код валюты, по которой нужно отфильтровать список.

Для получения описания операций, совершенных пользователем, введите список словарей, содержащих транзакции.

Для генерации номеров карт в заданном диапазоне введите стартовое и конечное числовые значения диапазона.

### Пример использования функции, которая фильтрует список словарей по статусу.

Подаем на вход: 
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

Получаем на выходе:
#### Выход функции со статусом по умолчанию 'EXECUTED'
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

#### Выход функции, если вторым аргументов передано 'CANCELED'
```
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

### Пример использования функции сортировки списка словарей по дате.

Подаем на вход: 
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

Получаем на выходе:
#### Выход функции (сортировка по убыванию, т.е. сначала самые последние операции)
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

### Пример использования функции обработки даты.

Подаем на вход:
```
2024-03-11T02:26:18.671407
```

Получаем на выходе:
```
11.03.2024
```

### Пример использования функции фильтрации транзакций.

Подаем на вход код валюты "USD" и список транзакций:
```
[
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
```

Получаем на выходе:
```
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```

### Пример использования генератора, возвращающего описание операций.

Подаем на вход список тот же список, что и для функции фильтрации транзакций (см выше). Получаем на выходе:

```
    Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```

### Пример использования генератора номеров карт

Подаем на вход значения start и stop в виде целых чисел в диапазоне от 0 до 9999999999999999, получаем на выходе список номеров карт в заданном диапазоне в формате:

```
    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```

## Тестирование:
В папке tests для каждого модуля создан тест.

- test_masks.py - тестирует правильность маскирования номера карты и номера счета.
- test_processing.py - тестирует функцию сортировки списка словарей по заданному статусу, функцию сортировки списка словарей по дате в порядке убывания или возрастания.
- test_widget.py - проверяется корректность распознавания и применения нужного тип маскировки в зависимости от типа входных данных (карта или счет) и правильности преобразования даты.
- test_generators.py:
    - тестирование функции filter_by_currency: корректно ли фильтруются транзакции по заданной валюте, правильно ли обрабатываются случаи, когда транзакции в заданной валюте отсутствуют, и не завершается ли генератор ошибкой при обработке пустого списка или списка без соответствующих валютных операций.
    - тестирование функции transaction_descriptions: возвращаются ли корректные описания для каждой транзакции, как работает функция с различным количеством входных транзакций, включая пустой список.
    - тестирование генератора card_number_generator: проверяем, что генератор выдает правильные номера карт в заданном диапазоне, корректно форматирует номера карт, корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.

## Документация:

Нет дополнительной информации.

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)