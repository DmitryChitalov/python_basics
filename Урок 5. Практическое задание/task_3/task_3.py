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

translation = dict(One='Один', Two='Два', Three='Три', Four='Четыре')
with open('nums.txt', encoding='utf-8') as my_file:
    for i in my_file:
        if i.split()[0] in translation:
            with open('output_file.txt', 'a', encoding='utf-8') as ouf:
                ouf.write(f'{translation[i.split()[0]]} - {i.split()[2]}\n')
