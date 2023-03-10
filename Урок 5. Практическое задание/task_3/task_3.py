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
f_n = []
try:
    with open('f.txt', 'r', encoding="utf-8") as file:
        with open('nf.txt', 'w', encoding="utf-8") as nf:
            lines = file.readlines()
            for line in lines:
                for k in num.keys():
                    if k in line:
                        f_n.append(line.replace(k, num[k]))
            nf.writelines(f_n)
except FileNotFoundError:
    print('Файл не найден.')