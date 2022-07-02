"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


new_text = []

while True:
    with open('file.txt', 'a', encoding='utf-8') as my_f:
        new_text = input("Введите текст: ")

        if new_text == '':
            break
        my_f.write(f"{new_text}\n")
