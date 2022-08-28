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
dict_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("test.txt", encoding='utf-8') as file:
    for line in file:
        for key in dict_rus.keys():
            line = line.replace(key, dict_rus[key])
        print(line)
        with open("file_rus.txt", "a", encoding='utf-8') as f_rus:
            f_rus.write(f"{line}")
