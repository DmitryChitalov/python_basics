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
translater = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("file4.txt", "r", encoding='utf-8') as file_4:
    content = file_4.readlines()
file_4.close()

with open("file4new.txt", "w+", encoding='utf-8') as file_4new:
    for el in content:
        english, number = el.split(" — ")
        tr = translater[english]
        file_4new.write(f"{tr} — {number}")
file_4new.close()
