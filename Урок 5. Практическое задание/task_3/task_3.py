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

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text3.txt', 'r', encoding='utf-8') as i:
    a = i.read()
    b = a
for el, el2 in dictionary.items():
    b = b.replace(el, el2)

with open('text3_1.txt', 'w', encoding='UTF-8') as new:
    new.write(b)
print('Готово!')
