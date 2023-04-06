"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""
my_str = "238 8971 345"
sum_of_numbers = 0

my_f = open("output_ex5.txt", "w")
my_f.write(my_str)
my_f.close()

my_f = open("output_ex5.txt", "r")
string = my_f.read()
my_list = list(string.split())
for i in my_list:
    sum_of_numbers = sum_of_numbers + int(i)
print(f"Сумма чисел = {sum_of_numbers}")
my_f.close()
