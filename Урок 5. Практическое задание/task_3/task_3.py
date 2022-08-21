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

my_file = open("c:\Python38\\text4.txt", "r", encoding="utf-8")
my_file_ru = open("c:\Python38\\text4_ru.txt", "w", encoding="utf-8")
str_replace = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

while True:
    line = my_file.readline()
    if not line:
        break
    for key in str_replace:
        line = line.replace(key, str_replace[key])
    my_file_ru.write(line)
my_file.close()
my_file_ru.close()
