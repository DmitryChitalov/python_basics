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
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('file1.txt', 'r', encoding='utf-8') as in_file:
    for line in in_file:
        for key in my_dict.keys():
            line = line.replace(key, my_dict[key])
        with open("file2.txt", "a", encoding='utf-8') as out_file:
            out_file.writelines(line)