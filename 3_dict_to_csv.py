"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

band = [
    {'name': 'Paul', 'age': 22, 'job': 'vocalist'},
    {'name': 'John', 'age': 23, 'job': 'guitarist'},
    {'name': 'George', 'age': 21, 'job': 'guitarist'},
    {'name': 'Richard', 'age': 23, 'job': 'drummer'}
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    with open('band.csv', 'w', newline='') as file:
        fieldnames = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for person in band:
            writer.writerow(person)


if __name__ == "__main__":
    main()
