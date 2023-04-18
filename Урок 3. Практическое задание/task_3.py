"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func_by_sort(arg1, arg2, arg3):
    arg_list = [arg1, arg2, arg3]
    arg_list.sort(reverse=True)
    return arg_list[0] + arg_list[1]

def my_func(arg1, arg2, arg3):
    big_one = arg1
    second_one = arg2
    if arg3 >= big_one:
        big_one = arg3
    elif arg3 >= second_one:
        second_one = arg3
    return big_one + second_one

num1 = float(input('Введите 1 число: '))
num2 = float(input('Введите 2 число: '))
num3 = float(input('Введите 3 число: '))

print(f'Сумма двух наибольших чисел через сортировку: {my_func_by_sort(num1, num2, num3)}')
print(f'Сумма двух наибольших чисел без сортировки: {my_func(num1, num2, num3)}')