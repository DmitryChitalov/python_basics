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

dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("One_Two_Three_Four.txt", "r", encoding='utf-8') as file:
    my_text_1 = file.read()
    for key, value in dictionary.items():
        my_text_1 = my_text_1.replace(key, value)
    with open("Один_Два_Три_Черыре.txt", "w", encoding='UTF-8') as file2:
        file2.write(my_text_1)