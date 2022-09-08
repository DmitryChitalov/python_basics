"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
digits = "1 2 3 4 5 6 7 8 9"
filename = "task5.txt"
my_summ = 0
with open(filename, 'w', encoding='utf-8') as file:
    file.write(digits)
with open(filename, encoding='utf-8') as file_2:
    data = file_2.read()

for item in data.split():
    my_summ += float(item)
print(f"Сумма - {my_summ}")


