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
out_f = open("dz_4.txt", "w", encoding='utf-8')
str_list = ['One — 1\n', 'Two — 2\n', 'Three — 3\n', 'Four — 4\n']
out_f.writelines(str_list)
out_f.close()

num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('dz_4.txt', 'r', encoding="utf-8") as file:
    with open('new_dz_4.txt', 'w+', encoding="utf-8") as new_file:
        for line in file:
            line_i = line.split()
            new_file.writelines(f'{num.setdefault(line_i[0])} {line_i[1]} {line_i[2]}\n')
