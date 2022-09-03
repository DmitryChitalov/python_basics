"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
list_num = open("data_file5.txt", "w")
print("Введите числа через пробелы: ")
while True:
    num = input()
    list_num.write(num + "\n")
    if num == "":
        break
list_num = open("data_file5.txt", "r")
tmp = list_num.read().split()
summ_num = 0
for i in tmp:
    summ_num += int(i)
print("Сумма чисел в файле: ", summ_num)
list_num.close()