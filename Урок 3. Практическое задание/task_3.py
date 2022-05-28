"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func_sort(a, b, c):
    args_lst = [a, b, c]
    args_lst.sort()
    return args_lst[1] + args_lst[2]

def my_func(a, b, c):
    args_lst = [a, b, c]
    min_element = a
    for item in args_lst:
        if item < min_element:
            min_element = item
    args_lst.remove(min_element)
    return args_lst[0] + args_lst[1]

numbers = input('Введите 3 числа через пробел ==>')
a = float(numbers.split()[0])
b = float(numbers.split()[1])
c = float(numbers.split()[2])
print('Сумма двух наибольших числе равна:\nС использованием sort():')
print(my_func_sort(a, b, c))
print('Без использования sort():')
print(my_func(a, b, c))
