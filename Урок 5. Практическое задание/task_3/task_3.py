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

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file3.txt', 'r', encoding='utf-8') as file_obj:
    content = file_obj.read().split('\n')
    for i in content:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)
with open('file3_new.txt', 'w+', encoding='utf-8') as file_obj2:
    file_obj2.writelines(new_file)
    file_obj2.seek(0)
    content2 = file_obj2.read()
    print(content2)

