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
trans = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open('text3.txt', 'r', encoding='UTF-8') as file_cont:
    new_file = file_cont.read()

new_file2 = new_file
for en, ru in trans.items():
    new_file2 = new_file2.replace(en, ru)

with open('text3_new.txt', 'w') as new_file_cont:
    new_file_cont.writelines(new_file2)
    print("Файл перезаписан")

