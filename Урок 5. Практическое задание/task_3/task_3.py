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
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('input_file.txt', 'r') as ifp:
    content = ifp.readlines()
    for i in content:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])

with open('output_file.txt', 'w') as ofp:
    ofp.writelines(new_file)
