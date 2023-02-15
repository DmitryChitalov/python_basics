"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_with_sort(arg1, arg2, arg3):
    """my func with sorted"""
    my_list = [arg1, arg2, arg3]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


def my_func_without_sort(arg1, arg2, arg3):
    """my func without sorted"""
    my_list = [arg1, arg2, arg3]
    my_list.remove(min(my_list))
    return sum(my_list)


print(f"Сумма наибольших двух аргументов из (5, -3, 12) = "
      f"{my_func_with_sort(5, -3, 12)} "
      f"с использованием sort()")


print(f"Сумма наибольших двух аргументов из (5, -3, 12) = "
      f"{my_func_without_sort(5, -3, 12)} "
      f"без использования sort()")

# * debug
# lst = input("Введите элементы списка: ").split()

# print(f"Сумма наибольших двух аргументов из ({lst[0]}, {lst[1]}, {lst[2]}) = "
#       f"{my_func_with_sort(int(lst[0]),int(lst[1]),int(lst[2]))} "
#       f"с использованием sort()")

# print(f"Сумма наибольших двух аргументов из ({lst[0]}, {lst[1]}, {lst[2]}) = "
#       f"{my_func_without_sort(int(lst[0]),int(lst[1]),int(lst[2]))} "
#       f"без использования sort()")
