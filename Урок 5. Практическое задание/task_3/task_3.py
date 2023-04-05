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
with open("nata3.txt", encoding='utf-8') as f:
    for str in f:
        for key in dict_num.keys():
            str = str.replace(key, dict_num[key])
        print(str)
        with open("nata3_1.txt", "a") as f_rus:
            f_rus.write(f"\n {str}")
