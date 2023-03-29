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

dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

num_en = ''
with open('new_3.txt', 'r', encoding='UTF-8') as file_en:
    num_en = file_en.read()

num_ru = num_en
for en, ru in dictionary.items():
    num_ru = num_ru.replace(en, ru)

with open('new_3.tmp', 'w', encoding='UTF-8') as file_ru:
    file_ru.write(num_ru)
