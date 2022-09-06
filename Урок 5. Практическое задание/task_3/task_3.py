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

data_int = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("data_in.txt", encoding='utf-8') as obj:
    for line in obj:
        for key in data_int.keys():
            line = line.replace(key, data_int[key])
        print(line)
        with open("data_output.txt", "a") as rus_word:
            rus_word.write(f"\n {line}")