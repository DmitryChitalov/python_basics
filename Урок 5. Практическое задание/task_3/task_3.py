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

rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text3.txt", "r+", encoding="utf-8") as text:
    with open("text3 (new).txt", "r+", encoding="utf-8") as newtext:
        newtext.writelines([el.replace(el.split()[0], rus.get(el.split()[0])) for el in text])
