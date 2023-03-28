"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
#!/usr/bin/env python3

def my_func1(arg_1, arg_2, arg_3):
    sorted_args = [arg_1, arg_2, arg_3]
    sorted_args.sort(reverse=True)
    return print(f"Используя функцию sort(): {sorted_args[0] + sorted_args[1]}.")
                 

def my_func2(arg_1, arg_2, arg_3):
    sorted_args = [arg_1, arg_2, arg_3]
    sorted_args.remove(min(sorted_args))
    return print(f"Без функции sort(): {sorted_args[0] + sorted_args[1]}.")

my_func1(12, 17, 25)
my_func2(12, 17, 25)
