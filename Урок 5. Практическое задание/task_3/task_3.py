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
with open('numbers.txt', 'r', encoding='utf-8') as usr_file:
    str_list = usr_file.read().split()

rus_numb = ['Один ', 'Два ', 'Три ', 'Четыре ']

del str_list[::3]

n = 0
for i in range(0, len(str_list) + 3, 3):
    str_list.insert(i, rus_numb[n])
    n += 1

for i in range(3, len(str_list), 4):
    str_list.insert(i, '\n')

with open('rus_numbers.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(' '.join(str_list))