"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

import requests

url = 'https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=1'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    try:
        response = requests.get(url, allow_redirects=True)
        with open('referat.txt', 'wb') as file:
            file.write(response.content)

        with open('referat.txt', 'r') as file:
            text = file.read()

        print('Text length:', len(text))
        print('Word count:', len(text.split()))

        text = text.replace('.', '!')

        with open('referat2.txt', 'w') as file:
            file.write(text)

    except requests.HTTPError as error:
        print(error)


if __name__ == "__main__":
    main()
