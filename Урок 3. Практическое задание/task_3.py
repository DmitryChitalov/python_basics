"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_one(first_obj, second_obj, third_obj):
    my_list = [first_obj, second_obj, third_obj]
    my_list.sort()
    print(f"Сумма наибольших двух аргументов (с использованием функции sort): "
          f"{my_list[1] + my_list[2]}")

def my_func_two(first_obj, second_obj, third_obj):
    if first_obj < second_obj and first_obj < third_obj:
        print(f"Сумма наибольших двух аргументов (без использованием функции "
              f"sort): {second_obj + third_obj}")
    elif first_obj > second_obj and first_obj < third_obj:
        print(f"Сумма наибольших двух аргументов (без использованием функции "
              f"sort): {first_obj + third_obj}")
    elif first_obj < second_obj and first_obj > third_obj:
        print(f"Сумма наибольших двух аргументов (без использованием функции "
              f"sort): {first_obj + second_obj}")

my_func_one(50, 35, 8)
my_func_two(40, 35, 80)
