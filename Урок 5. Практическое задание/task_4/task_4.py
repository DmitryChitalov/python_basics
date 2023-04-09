"""
4.	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os

path = os.path.dirname(__file__)


def write_file(input_list):
    with open((os.path.join(path, 'dst_file.txt')), 'a', encoding='utf-8') as file_w:
        file_w.writelines(" ".join(input_list) + "\n")


try:
    with open((os.path.join(path, 'src_file.txt')), 'r', encoding='utf-8') as file_r:
        for line in file_r:

            a = line.split()

            if a[0] == "One":
                a[0] = "Один"
                write_file(a)
            elif a[0] == "Two":
                a[0] = "Два"
                write_file(a)
            elif a[0] == "Three":
                a[0] = "Три"
                write_file(a)
            elif a[0] == "Four":
                a[0] = "Четыре"
                write_file(a)
            if '' == a[0].rstrip():
                continue
except:
    print("В файле присутствует пустая строка")
