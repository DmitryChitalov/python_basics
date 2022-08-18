"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

text = input("Введите числа разделяя пробелом --> ")

with open("file_5.txt", "w", encoding="utf-8") as f_obj:
    print(text, file=f_obj)

with open("file_5.txt", "r", encoding="utf-8") as f_obj:
    numbers = [int(el) for el in f_obj.read().split()]

print(f"Сумма введенных чисел: {sum(numbers)}")
