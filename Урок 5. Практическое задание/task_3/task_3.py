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
word_change = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_ru = []
with open("data_file3_1.txt", "r") as df1:
    for i in df1:
        i = i.split(" ", 1)
        file_ru.append(word_change[i[0]] + " " + i[1])
    print(file_ru)

with open("data_file3_2.txt", "w") as df2:
    df2.writelines(file_ru)