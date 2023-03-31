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
os.getcwd()
print("Уточняю расположение файла вывода функцией os.getcwd():", os.getcwd())


input_data = open("./input_file3.txt", "r")
lines_in_file = 0
words_in_line = 0
counting_lines = {}

for i in input_data:
    lines_in_file +=1


print(f"{lines_in_file} и {words_in_line}.")

input_file.close()
