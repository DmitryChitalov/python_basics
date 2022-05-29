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
number = {"1": "Один", "2": "Два", "3": "Три", "4": "Четыре"}
result = []
with open("input.txt", "r", encoding='utf-8') as file:
    for line in file:
        num = line.split()[-1]
        result.append(" - ".join([number.get(num), num]) + "\n")

with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(result)
