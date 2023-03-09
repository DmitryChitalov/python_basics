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

num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_text = []
try:
    with open('file.txt', 'r', encoding="utf-8") as file:
        with open('new_file.txt', 'w', encoding="utf-8") as new_file:
            lines = file.readlines()
            for line in lines:
                for k in num.keys():
                    if k in line:
                        new_text.append(line.replace(k, num[k]))
            new_file.writelines(new_text)
except FileNotFoundError:
    print('Файл не найден.')