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

russian_dict = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}
lines_count = 0
lines_to_write = []
interpreters_line = ""

with open("input_file3.txt", 'r') as source_file:
    source_content = source_file.readlines()

    for i in source_content:
        interpreters_line = (russian_dict.get(source_content[lines_count]), source_content[1:])
        lines_count += 1
        print(interpreters_line)

# with open("output_file.txt", "w", encoding="UTF-8") as output_file:
#     output_file.write(output_data)

#     for i in source_content:
#         output_data = open("output_file3.txt", "+a", encoding="UTF-8")
#         output_data.write
#         output_data.close()
#         lines_count += 1
