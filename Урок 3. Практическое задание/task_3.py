"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
#
# с использованием функции sorted
def my_func(*args):
    print(sum(sorted(list(args), reverse = True)[:2]))

ONLY_TWO_ELEMENTS = 2 # константа для функции my_func_without_sort
# без использования функции sorted
def my_func_without_sort(*args):
    my_list = list(args)
    i = 0
    result = 0
    while i != ONLY_TWO_ELEMENTS:
        max_num = max(my_list)
        result += max_num
        my_list.remove(max_num)
        i += 1
    return result

my_func(55, 5, 2, 509)

print(my_func_without_sort(55, 5, 2, 509))






