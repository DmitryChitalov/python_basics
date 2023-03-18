a = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

a_en = ''
with open("file1.txt", "r", encoding='UTF-8') as b_en:
    a_en = b_en.read()

a_ru = a_en
for en, ru in a.items():
    a_ru = a_ru.replace(en, ru)

with open("file2.txt", "w", encoding='UTF-8') as b_ru:
    b_ru.write(a_ru)

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
