"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func_with_sort():
    num1, num2, num3 = int(input('Введите первое число: ')), int(input('Введите второе число: ')), \
        int(input('Введите третье число: '))
    sort_list = [num1, num2, num3]
    sort_list.sort(reverse=True)
    res_sum = sort_list[0] + sort_list[1]
    return res_sum
def my_func_witout_sort():
    num1, num2, num3 = int(input('Введите первое число: ')), int(input('Введите второе число: ')), \
        int(input('Введите третье число: '))
    sort_list = [num1, num2, num3]
    sort_list.remove(min(sort_list))
    res_sum = sum(sort_list)
    return res_sum
try:
    print(f'Сумма наибольших двух чисел с сортировкой: {my_func_with_sort()}')
    print(f'Сумма наибольших двух чисел без сортировки: {my_func_witout_sort()}')
except ValueError:
    print('Нужно ввести числа')


