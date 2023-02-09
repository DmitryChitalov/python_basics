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
lib_locale = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_txt_file = []
with open('numbers.txt', 'r', encoding='utf-8') as txt_file:
    for i in txt_file:
        i = i.split(' ', 1)
        new_txt_file.append(lib_locale[i[0]] + ' ' + i[1])

with open('numbers2.txt', 'w', encoding='utf-8') as txt_file2:
    txt_file2.writelines(new_txt_file)
