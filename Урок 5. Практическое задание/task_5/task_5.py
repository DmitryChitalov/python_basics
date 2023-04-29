"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
numbers_add = ''
while True:
    nums_user = input('Введите число: ')
    if nums_user == '':
        break
    numbers_add = numbers_add + nums_user + ' '
with open('numbers.txt', 'w', encoding='utf-8') as numbers:
    numbers.write(numbers_add)

with open('numbers.txt', encoding='utf-8') as number:
    nums = number.read().split()

nums = [int(nums) for nums in nums]
print(f'Сумма чисел в файле - {sum(nums)}')