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


translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

with open('task_3_input.txt', 'r', encoding="utf-8") as f1:
    with open('task_3_output.txt', 'w', encoding="utf-8") as f2:
        lines = f1.readlines()
        for i in lines:
            i = i.split(' ', 1)
            new_file.append(translate[i[0]] + ' ' + i[1])
        f2.writelines(new_file)
