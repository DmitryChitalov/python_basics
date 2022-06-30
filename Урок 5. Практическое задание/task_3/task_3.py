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

translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("test_3.txt", "r") as file_from:
    with open("test_3_new.txt", "w") as file_to:
        lines = file_from.readlines()
        file_info = []
        for line in lines:
            line = line.split(' ', 1)
            file_info.append(translation[line[0]] + '  ' + line[1])
        file_to.writelines(file_info)
