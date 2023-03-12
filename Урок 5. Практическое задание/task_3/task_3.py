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

def translate(line):
    translate_map = {
        "One": "Один", 
        "Two": "Два", 
        "Three": "Три",
        "Four": "Четыре",
        "Five": "Пять",
        "Six": "Шесть", 
        "Seven": "Семь",
        "Eight": "Восемь",
        "Nine": "Девять"
    }

    result = line
    for key in translate_map:
        result = result.replace(key, translate_map[key])
    return result

# clear output file
open("output.txt", "w", encoding="utf-8").close()

with open("input.txt", "r", encoding="utf-8") as in_file:
    for line in in_file:
        line = translate(line)
        print(line)
        with open("output.txt", "a", encoding="utf-8") as out_file:
            out_file.write(line)


