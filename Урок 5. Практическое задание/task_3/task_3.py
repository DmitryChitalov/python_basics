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

with open('input.txt', 'r') as input_file:
    with open('output.txt', 'w') as output_file:
        translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        for line in input_file:
            parts = line.split(' — ')
            if len(parts) == 2:
                russian_number = translation.get(parts[0])
                if russian_number:
                    parts[0] = russian_number
                output_file.write(' — '.join(parts))

print('Новый блок строк записан в файл output.txt.')
