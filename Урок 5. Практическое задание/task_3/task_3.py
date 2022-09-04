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

dct = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task3.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in dct.keys():
            line = line.replace(key, dct[key])
        print(line)
        with open("task3_1.txt", "a", encoding='utf-8') as f_new:
            f_new.write(line)
