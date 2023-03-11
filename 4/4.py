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

translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять'
}

with open('file_for_task.txt', 'r', encoding='utf-8') as f_1:
    for line in f_1:
        key = line.split()[0]
        new_string = line.replace(key, translate_dict[key])

        with open('result.txt', 'a', encoding='utf-8') as f_2:
            f_2.writelines(new_string)