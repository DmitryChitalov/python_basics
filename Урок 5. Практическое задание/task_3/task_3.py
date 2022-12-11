"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
Псываться в новый три этом английские числительные должны заменяться на русские.
Новый блок строк должен запиекстовый файл.
"""
my_string = """One — 1
Two — 2
Three — 3
Four — 4"""
with open("in.txt", "w", encoding="UTF-8") as f:
    f.write(my_string)
with open("in.txt", "r", encoding="UTF-8") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].replace("One", "Один").replace("Two", "Два").replace("Three", "Три").replace("Four", "Четыре")

with open("out.txt", "w", encoding="UTF-8") as f:
    f.writelines(data)
