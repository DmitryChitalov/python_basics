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
#!/usr/bin/env python3
import os
print("Внимание, текущая папка:", os.getcwd())

russian_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
line_to_write = ""
block_to_write = []

with open("input_file3.txt", 'r') as source_file:
    source_content = source_file.readlines()

    for i in source_content:
        line_to_write = russian_dict.get(i.split()[0]), " ".join(i.split()[1:])
        line_to_write = " ".join(line_to_write)
        block_to_write.append(line_to_write)
        
with open("output_file3.txt", "w", encoding="UTF-8") as output_file:
    for j in block_to_write:
        output_file.write(f"{j}\n")
