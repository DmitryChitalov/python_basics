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
dict_num = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

my_f = open("input.txt", "r", encoding='utf-8')
new_f = open("output.txt", "w")
for string in my_f:
    for key in dict_num.keys():
        string = string.replace(key, dict_num[key])
    new_f.write(string)
my_f.close()
new_f.close()