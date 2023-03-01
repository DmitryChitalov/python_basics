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

dictionary = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

source = []
with open("source.txt", "r", encoding="UTF-8") as fp:
    source = fp.read()

target = source
for find, replace in dictionary.items():
    print(f"Замена '{find}' на '{replace}'")
    target = target.replace(find, replace)

with open("target.txt", "w") as fp:
    fp.writelines(target)
