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

my_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('file.txt', encoding='utf-8') as file:
    for l in file:
        for k in my_dic.keys():
            l = l.replace(k, my_dic[k])
        print(l)
        with open('nfile.txt', 'a', encoding='utf-8') as n_file:
            n_file.write(f'{l}')