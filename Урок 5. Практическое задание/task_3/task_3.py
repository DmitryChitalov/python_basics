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
file_u = open("numers.txt", "r")
file_o = open("numersrus.txt", "w")
for line in file_u:
    print(line)
    if (line[-2]) == "1":
        file_o.write("Один - 1"+ '\n')
    elif (line[-2]) == "2":
        file_o.write("Два - 2"+ '\n')
    elif (line[-2]) == "3":
        file_o.write("Три - 3"+ '\n')
    elif (line[-2]) == "4":
        file_o.write("Четыре - 4"+ '\n')
file_u.close()
file_o.close()

