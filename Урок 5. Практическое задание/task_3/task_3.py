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
my_dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("test.txt", encoding='utf-8') as start_file:
    for i in start_file:
        for k in my_dictionary.keys():
            i = i.replace(k, my_dictionary[k])
        print(i)
        with open("finally_file.txt", "a") as finally_file:
            finally_file.write(f"\n {i}")