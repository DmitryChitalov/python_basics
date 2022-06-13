"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def writeToRu(line):
    with open('result.txt', 'a', encoding='utf-8') as f_ru:
        f_ru.write(f'{line}')


with open('text.txt', 'r', encoding='utf-8') as f_en:
    for line in f_en:
        spl = line.split(' ')
        ru_line = line.replace(spl[0], dictionary.get(spl[0]))
        writeToRu(ru_line)
