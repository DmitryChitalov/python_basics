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
with open('file.txt', 'r', encoding="utf8") as f:
    file_list = f.readlines()
my_dict = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}
with open('out_file.txt', 'w', encoding='utf8') as f:
    for el in file_list:
        a = el.split()
        print(f'{my_dict.get(a[0])} {a[1]} {a[2]}', file=f)
