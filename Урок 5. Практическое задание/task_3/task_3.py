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
num_dict = {'Four': 'Четыре', 'Two': 'Два', 'Three': 'Три', 'One': 'Один'}
source_file = open("test_file_1.txt", "r", encoding='utf-8')
new_file = open("test_file_2.txt", "w", encoding='utf-8')
for line in source_file:
    print(f'eng {line}')
    for key in num_dict.keys():
        line = line.replace(key, num_dict[key])
    print(f'rus {line}')
    new_file.write(line)

source_file.close()
new_file.close()
