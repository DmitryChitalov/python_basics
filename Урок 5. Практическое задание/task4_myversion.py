"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
"""Открывается созданный заранее файл на чтение"""


def rewrite():
    number = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    try:
        with open('file4.txt', 'r+', encoding="utf-8") as file:
            """Создается новый файл на чтение и запись"""
            with open('new_file4.txt', 'r+', encoding="utf-8") as new_file:
                text = file.readlines()
                """Создается текст нового файла с измененными данными"""
                for i in text:
                    i = i.split(' ', 1)
                    new_text.append(number[i[0]] + ' ' + i[1])
                new_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite()
