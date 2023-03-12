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



import codecs

# Создаем словарь с заменами
replace_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with codecs.open('input.txt', 'r', encoding='utf-8') as input_file,\
     codecs.open('output.txt', 'w', encoding='utf-8') as output_file:
    for line in input_file:
        for key, value in replace_dict.items():
            line = line.replace(key, value)
        output_file.write(line)
