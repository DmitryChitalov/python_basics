"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


#Решение задачи без использования функции sort()
def my_func(arg1, arg2, arg3):

    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2     
    if arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3    
    if arg1 < arg2 and arg1 < arg3:
        return arg2 + arg3


arg1 = int(input("Введите первое число: "))
arg2 = int(input("Введите второе число: "))
arg3 = int(input("Введите третье число: "))

print(f"Сумма наибольших чисел: {my_func(arg1, arg2, arg3)}")

#Решение задачи с использованием функции sort()

def my_funk(arg1, arg2, arg3):

    my_list = [arg1, arg2, arg3]
    my_list.sort()
    return sum(my_list[1:])


arg1 = int(input("Введите первое число: "))
arg2 = int(input("Введите второе число: "))
arg3 = int(input("Введите третье число: "))

print(f"Сумма наибольших чисел: {my_funk(arg1, arg2, arg3)}")