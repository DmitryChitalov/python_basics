# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

voc = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('dz5_4.txt', 'r') as my_file:
    # content = my_file.read().split('\n')
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(voc[i[0]] + ' ' + i[1].strip())
    print(new_file)

with open('dz5_4_new.txt', 'w') as my_file2:
    my_file2.writelines(new_file)
