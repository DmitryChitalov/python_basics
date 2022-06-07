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

wr_fi = []
sp = ['один', 'два', 'три', 'четыре']
with open('new_f.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        read_str = line.split()
        read_str[0] = sp[i]
        wr_fi.append(read_str)
    print(wr_fi)

with open('new_f_rus', 'w', encoding='utf-8') as file:
    for i in wr_fi:
        file.write(' '.join(i))
        file.write('\n')
        print(i)

