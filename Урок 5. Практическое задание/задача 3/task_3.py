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
replace = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

fr = open("file.txt", "r")
fw = open("translate.txt", "w")

for line in fr:
    for dict_key in replace:
        line = line.replace(dict_key, replace.get(dict_key))

    fw.write(line)

fr.close()
fw.close()
