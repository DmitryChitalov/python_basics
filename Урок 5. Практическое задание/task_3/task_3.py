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

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("HW5_task3.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in my_dict.keys():
            line = line.replace(key, my_dict.get(key))
        print(line)
        with open("HW5_task3.1.txt", "a", encoding='utf-8') as f_obj2:
            f_obj2.write(line)


