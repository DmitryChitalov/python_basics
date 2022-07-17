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

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
my_file = []
with open('my_file_eng.txt', 'r', encoding='utf-8') as f:
  for i in f:
      i = i.split(' ', 1)
      my_file.append(rus[i[0]] + ' ' + i[1])

with open('my_file_rus.txt', 'w', encoding='utf-8') as new_file:
    new_file.writelines(my_file)
