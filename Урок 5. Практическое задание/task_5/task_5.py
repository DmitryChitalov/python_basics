"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('test5.txt', 'w', encoding='utf-8') as test5:
    number = input()
    test5.write(number)

    number_sum = sum(int(i) for i in number.split())
    print(f'Сумма: {number_sum}')