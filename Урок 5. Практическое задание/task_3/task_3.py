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
new_file = rus
with open('text3.txt', 'r') as file_obj:
    content = file_obj.readlines()
    for i in file_obj:
        #append_line = rus + '\n'
        #i = i.split(' \n ', 1)
        new_file.append(rus[i[0]] + '\n' + i[1])

with open('text3.txt', 'w') as file_obj:
    file_obj.writelines(str(new_file))
    print(new_file)

