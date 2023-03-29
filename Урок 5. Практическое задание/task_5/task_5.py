"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('some_numbers.txt', 'w', encoding='UTF-8') as file:
    numbers = input("Введите несколько чисел через пробел: ")
    file.write(numbers)
    final_sum = sum(int(value) for value in numbers.split())
    print(f'Сумма введенных чисел: {final_sum}')
