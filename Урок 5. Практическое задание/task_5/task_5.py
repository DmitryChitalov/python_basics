"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('numbers.txt', 'w', encoding='utf-8') as file:
    numbers = input('Введите числа разделённые пробелом: ')
    file.write(numbers)

    num_sum = sum(int(n) for n in numbers.split())
    print(f'Сумма чисел записанная в файл nubmers.txt: {num_sum}')
