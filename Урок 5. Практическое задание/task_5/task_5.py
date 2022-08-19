"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
numbers = "1 3 5 7"
result_sum = 0
with open("numbers.txt", "w", encoding="utf-8") as f_write:
    f_write.write(numbers)

with open("numbers.txt", "r", encoding="utf-8") as f_read:
    for n in f_read.readline().split(' '):
        result_sum += int(n)
    print(f"Сумма чисел: {result_sum}")

