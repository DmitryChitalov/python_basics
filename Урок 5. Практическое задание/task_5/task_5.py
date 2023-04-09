"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

result = 0
with open('digit_file.txt', 'w', encoding='utf-8') as file:
    for i in range(randint(5, 10)):
        number = randint(0, 100)
        file.write(str(number) + ' ')
        result += int(number)

print(f"Сумма чисел = {str(result)}")
