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
my_f = open("task3.txt", encoding='utf-8')
i = 0
my_list = []
for i in my_f.readlines():
    i = i.replace("One", "Один")
    i = i.replace("Two", "Два")
    i = i.replace("Three", "Три")
    i = i.replace("Four", "Четыри")
    my_list.append(i)
my_f.close()
out_f = open("task3_new.txt", "w", encoding='utf-8')
out_f.writelines(my_list)
out_f.close()
