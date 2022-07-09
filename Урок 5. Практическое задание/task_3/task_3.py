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

translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("file_3.txt") as f_obj:
    RESULT = ''
    for line in f_obj:
        part = line.split(" — ")
        print(part)
        if part[0] in translater:
            word = translater[part[0]]
            RESULT = word + ' — ' + part[1]
            with open("file_output_3.txt", "a") as f_2_obj:
                f_2_obj.writelines(RESULT)
