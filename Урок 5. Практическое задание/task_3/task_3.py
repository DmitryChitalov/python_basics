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

dict_int = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("input_file.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in dict_int.keys():
            line = line.replace(key, dict_int[key])
        print(line)
        with open("output_file.txt", "a") as f_rus:
            f_rus.write(f"\n {line}")

