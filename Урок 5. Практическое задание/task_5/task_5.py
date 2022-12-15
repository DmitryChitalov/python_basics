"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
numbers = "10 20 30 40 50 100 1 1000"
with open("5.txt", "w", encoding="UTF-8") as numb:
    numb.write(numbers)
with open("5.txt", "r", encoding="UTF-8") as numb:
    data = numb.readline().split()
    data = sum([float(x) for x in data])
print(data)
