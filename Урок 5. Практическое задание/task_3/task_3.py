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
num_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open(r"C:\Users\Serg\Desktop\fff.txt", 'r') as my_file:
    for line in my_file:
        for key in num_rus.keys():
            line = line.replace(key, num_rus[key])
        print(line)
        with open(r"C:\Users\Serg\Desktop\new_text.txt", 'a') as new_file:
            new_file.write(line)
