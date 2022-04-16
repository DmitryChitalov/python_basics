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

numbers_translate = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

def line_replace(line) -> str:
    for key in numbers_translate:
        line = line.replace(key, numbers_translate[key])
    
    return line

with open("task3_input.txt", "r", encoding = "utf-8") as file_input:
    with open("task3_output.txt", "w", encoding = "utf-8") as file_output:
        line = file_input.readline()
        while line != "":
            file_output.write(line_replace(line))
            line = file_input.readline()