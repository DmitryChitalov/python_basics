"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
numbers = "12 23 97 924 490309 2 4590 454542 00987 422 575362 23845 24289 537853"
with open("out.txt", "w", encoding="UTF-8") as f:
    f.write(numbers)
with open("out.txt", "r", encoding="UTF-8") as f:
    data = f.readline().split()
    data = sum([float(x) for x in data])
print(data)
