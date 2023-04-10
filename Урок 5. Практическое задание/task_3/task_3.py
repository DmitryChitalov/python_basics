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
f_obj = open(r"D:\DevOps\Python\Урок5\test3.txt", "r")
s_obj = open(r"D:\DevOps\Python\Урок5\test4.txt", "w")

for line in f_obj:
  line = line.replace("One", "один")
  line = line.replace("Two", "два")
  line = line.replace("Three", "три")
  line = line.replace("Four", "четыре")
  s_obj.write(line)


f_obj.close()
s_obj.close()