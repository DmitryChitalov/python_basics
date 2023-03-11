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
dict_ = {"One": "Один",
         "Two": "Два",
         "Three": "Три",
         "Four": "Четыре"}

i = 0
str_list = []
with open("file.txt") as f_obj:
    for line in f_obj:
        str_list.append(line.replace(list(dict_.keys())[i], list(dict_.values())[i]))

        i += 1
out_f = open("out_file.txt", "w")
out_f.writelines(str_list)
# print(line, end="")
