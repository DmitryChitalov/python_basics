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
count_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
f_obj = open("t3in.txt", encoding="utf8")
f_obj1 = open("t3out.txt", "w")
my_list = []

for line in f_obj:
    my_list = line.split()
    my_list[0] = count_dict.get(my_list[0])
    f_obj1.write(" ".join(my_list))
    f_obj1.write("\n")

f_obj.close()
f_obj1.close()
