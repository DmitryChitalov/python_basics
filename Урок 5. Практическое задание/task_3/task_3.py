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

# pylint: disable=consider-using-dict-items disable=line-too-long

repl = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("en.txt", "r", encoding="utf8") as en_file, open("ru.txt", "a", encoding="utf-8") as ru_file:
    for line in en_file:
        for el in repl:
            line = line.replace(el, repl[el])
        ru_file.write(line)
