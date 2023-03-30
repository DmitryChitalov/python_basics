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
try:
    with open("test_file.txt") as f_obj:
        dest_file = open("dest_file.txt", "w")
        for line in f_obj:
            data_from_line = line.split()
            if data_from_line[0] == "One":
                dest_file.write(line.replace("One","Один"))
            elif data_from_line[0] == "Two":
                dest_file.write(line.replace("Two", "Два"))
            elif data_from_line[0] == "Three":
                dest_file.write(line.replace("Three", "Три"))
            elif data_from_line[0] == "Four":
                dest_file.write(line.replace("Four", "Четыре"))
            else:
                print("Nothing to change")
        #    dest_file.write(line)
        dest_file.close()
except IOError:
    print("проблема с открытием файла. возможно его нет")
print("done")
