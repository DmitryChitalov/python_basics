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
replaces = {'One':'Один' ,'Two':'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('first.txt', 'r', encoding='utf-8') as eng:
    words_1 = eng.read()
words_2 = words_1
for k, v in replaces.items():
    words_2 = words_2.replace(k, v)
with open('second.txt', 'w') as rus:
    rus.write(words_2)