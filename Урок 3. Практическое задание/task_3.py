"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def sum_two_biggest_numbers_v1(first_arg, second_arg, third_arg):
    lst = [first_arg, second_arg, third_arg]
    return sum(lst) - min(lst)


def sum_two_biggest_numbers_v2(first_arg, second_arg, third_arg):
    lst = [first_arg, second_arg, third_arg]
    lst.sort()
    return lst[1] + lst[2]


first_numb = int(input("Введите первое число: "))
second_numb = int(input("Введите второе число: "))
third_numb = int(input("Введите третье число: "))

print(f'Без сортировки: {sum_two_biggest_numbers_v1(first_numb, second_numb, third_numb)}')
print(f'С сортировкой: {sum_two_biggest_numbers_v2(first_numb, second_numb, third_numb)}')
