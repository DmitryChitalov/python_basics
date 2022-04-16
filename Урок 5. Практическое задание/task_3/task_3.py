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
my_translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
try:
    with open('test.txt', 'r', encoding='utf-8') as my_file, open('test_out.txt', 'w', encoding='utf-8') as my_file_out:
        for line in my_file:
            for src, target in my_translate.items():
                line = line.replace(src, target)
            my_file_out.write(line)
except FileNotFoundError:
    print(f'Error file')
