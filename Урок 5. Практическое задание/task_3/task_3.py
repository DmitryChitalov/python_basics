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

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text.txt", "r", encoding="utf-8") as my_file:
    for el in my_file:
        for my_key in my_dict.keys():
            el = el.replace(my_key, my_dict[my_key])
        with open("import_text.txt", "a", encoding="utf-8") as my_file_1:
            print(el, file=my_file_1)


