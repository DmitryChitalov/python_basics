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
dictinnary_num = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("input_file.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in dictinnary_num.keys():
            line = line.replace(key, dictinnary_num[key])
        print(line)
        with open("output_file.txt", "a") as f_translate:
            f_translate.write(f"\n {line}")