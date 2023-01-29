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


with open('digits.txt', 'r') as my_file:
    my_list = my_file.read().split('\n')
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for lines in my_list:
        res = lines.split()
        with open('result.txt', 'a', encoding='utf_8') as f:
            f.writelines(f"{my_dict[res[0]]} {res[1]} {res[2]}\n")

