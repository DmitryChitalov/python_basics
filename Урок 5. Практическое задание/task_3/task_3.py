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
with open('my_file3.txt', 'r', encoding='utf-8') as my_file:
    my_string = []
    for line in my_file:
        my_string.append(line.split(' '))


my_numb = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

for line in my_string:
    if line[0] in my_numb:
        line[0] = my_numb[line[0]]


with open('my_new3.txt', 'w', encoding='utf-8') as my_file:
    for line in my_string:
        my_file.writelines(' '.join(line))
