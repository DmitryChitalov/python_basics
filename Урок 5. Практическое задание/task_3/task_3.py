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
#Lines = ["One — 1\n","Two — 2\n","Three — 3\n","Four — 4\n"]
 
file1 = open('english.txt', 'r')
Lines = file1.readlines()
 
dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
count = 0
for line in Lines:
    count += 1
    print("English Line{}: {}".format(count, line))
    for key, value in dictionary.items():
        line = line.replace(key, value)
    print("Russian Line{}: {}".format(count, line))

file1 = open('russian.txt', 'w')
file1.writelines(Lines)
file1.close()
