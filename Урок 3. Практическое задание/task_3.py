"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

first_number = int(input('Enter first number '))
second_number = int(input('Enter second number '))
third_number = int(input('Enter third number '))


def my_func(first_number, second_number, third_number):
    numbers = [first_number, second_number, third_number]
    result = []
    first_max_num = max(numbers)
    result.append(first_max_num)
    numbers.remove(first_max_num)
    second_max_num = max(numbers)
    result.append(second_max_num)
    print(f'Sum of the largest number is {sum(result)}')


my_func(first_number, second_number, third_number)
