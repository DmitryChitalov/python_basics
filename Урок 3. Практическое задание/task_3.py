"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

import string_extension

def my_func_with_sort(var_1, var_2, var_3):
    if string_extension.is_float(var_1) & string_extension.is_float(var_2) & string_extension.is_float(var_3):
        num_list = [float(var_1), float(var_2), float(var_3)]
        num_list.sort(reverse=True)
        
        return num_list[0] + num_list[1]
    else:
        print("Error: one of function arguments is not a number")


def my_func_without_sort(var_1, var_2, var_3):
    if string_extension.is_float(var_1) & string_extension.is_float(var_2) & string_extension.is_float(var_3):
        num_1 = float(var_1)
        num_2 = float(var_2)
        num_3 = float(var_3)

        return num_1 + num_2 + num_3 - min(num_1, num_2, num_3)
    else:
        print("Error: one of function arguments is not a number")

input_var_1 = input("Please input first number: ")
input_var_2 = input("Please input second number: ")
input_var_3 = input("Please input third number: ")

print(f"Sum of two max number is: {my_func_with_sort(input_var_1, input_var_2, input_var_3)}")
print(f"Sum of two max number is: {my_func_without_sort(input_var_1, input_var_2, input_var_3)}")