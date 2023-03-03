"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# решение с использованием сортировки
def my_func(var_1, var_2, var_3):
    my_vars = (var_1, var_2, var_3)
    my_list = list(my_vars)
    my_list.sort(reverse=True)
    result = int(my_list[0]) + int(my_list[1])
    return result

# решение без использования сортировки
def my_altfunc(var_1, var_2, var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        result = var_1 + var_2
    elif var_1 >= var_2 and var_3 >= var_2:
        result = var_1 + var_3
    elif var_2 >= var_1 and var_3 >= var_1:
        result = var_2 + var_3
    return result

print(my_func(6, 67, 8))
print(my_altfunc(67, 8, 6))
