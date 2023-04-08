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

num = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
updated = []
i = 0
with open("lesson5-3.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        lines = line.split(" ", 1)
        if lines[0] in num:
            rus = num[lines[0]]
            updated.append(rus + lines[1])
            i = i + 1
    print(updated)
with open("result5-3.txt", "w") as my_file2:
    my_file2.writelines(updated)