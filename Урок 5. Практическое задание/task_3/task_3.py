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

eng_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('list_1.txt', 'r') as list_obj:
    for i in list_obj:
        i = i.split(' ', 1)
        new_list.append(eng_ru[i[0]] + '  ' + i[1])
    print(new_list)

with open('list_1_new.txt', 'w') as list_obj_2:
    list_obj_2.writelines(new_list)
