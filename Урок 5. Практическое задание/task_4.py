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

input_file = open("file4.txt", encoding='utf-8')
output_file = open("file4_2.txt", "w", encoding='utf-8')

# Не додумался решить задачу через словарь, потом у Вас увидел, что можно было.

for line in input_file:
    if line.__contains__('One'):
        output_file.write(line.replace('One', 'Один'))
    if line.__contains__('Two'):
        output_file.write(line.replace('Two', 'Два'))
    if line.__contains__('Three'):
        output_file.write(line.replace('Three', 'Три'))
    if line.__contains__('Four'):
            output_file.write(line.replace('Four', 'Четыре'))


input_file.close()
output_file.close()
