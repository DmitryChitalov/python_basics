"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def get_words(line_text):
    """
    Функция возвращает количество слов в строке
    :param line_text: текстовая строка
    :return:
    Пример вызова: get_words("Моя текстовая строка")
    - > 3
    """

    try:
        return len(line_text.strip().split(' '))
    except BaseException as err:
        print(f"General error: {err}")


try:
    with open("data.txt", encoding="utf-8") as f:
        for num, line in enumerate(f, 1):
            print(f"Строка № {num}, слов в строке: {get_words(line)}")

except IOError as e:
    print(f"IOError: {e}")
