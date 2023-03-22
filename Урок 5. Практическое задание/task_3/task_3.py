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

num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три',
            'Four': 'Четыре', 'Five': 'Пять'}

new_dict = []
with open('ex3.txt', 'r', encoding='utf-8') as file1:
    for elem in file1:
        elem = elem.split(' ', 1)
        new_dict.append(num_dict[elem[0]] + '  ' + elem[1])

with open('ex3res.txt', 'w', encoding='utf-8') as file2:
    file2.writelines(new_dict)
