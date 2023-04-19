"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
file = open("test.txt", "w+", encoding='utf-8')
file.write(input())
file.close()
sumOfElements = 0
with open("test.txt") as f:
    for line in f:
        list_length = len(line.split())
        for i in range(list_length):
            sumOfElements = sumOfElements+int(line.split()[i])
print(sumOfElements)



