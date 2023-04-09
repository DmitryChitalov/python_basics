"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('my_number.txt', 'w', encoding='UTF-8') as file:
    number = input("Введите числа через пробел: ")
    file.write(number)
    final = sum(int(value) for value in number.split())
    print(f'Сумма выбранных чисел: {final}')

