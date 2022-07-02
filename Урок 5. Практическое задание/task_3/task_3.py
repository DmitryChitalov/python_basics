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


with open('file.txt', 'r', encoding='utf-8') as my_f:
    text = my_f.read()
text = text.replace("One", "Один").\
    replace("Two", "Два").replace("Three", "Три").replace("Four", "Четыре")
with open("file2.txt", "w", encoding='utf-8') as my_f2:
    my_f2.write(text)
