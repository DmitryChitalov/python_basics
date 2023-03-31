"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
f_obj = open("new_file.txt", "w+")
f_obj.write(input("Введите строку из целых чисел, разделенных пробелами:"))
f_obj.seek(0)
content = f_obj.readline()
my_list = content.split()
res = 0

for el in my_list:
    print(el)
    res += int(el)

f_obj.close()
print(f"Сумма всех чисел в файле: {res}")
