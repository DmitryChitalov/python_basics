"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# Функция возвращает сумму наибольших двух аргументов, используя функцию sort()
def my_func_1(argument_1, argument_2, argument_3):
    my_list = [argument_1, argument_2, argument_3]
    my_list.sort()
    return my_list[-1] + my_list[-2]

# Функция возвращает сумму наибольших двух аргументов, не используя функции sort()
def my_func_2(argument_1, argument_2, argument_3):
    return max(argument_1, argument_2, argument_3) + \
        max(min(argument_1, argument_2), min(argument_1, argument_3), min(argument_2, argument_3))

try:
    argument_1 = float(input("Введите первое число: "))
    argument_2 = float(input("Введите второе число: "))
    argument_3 = float(input("Введите третье число: "))
except ValueError:
    print("Ошибочный ввод!")
else:
    print(f"Результат с функцией sort(): {my_func_1(argument_1,argument_2,argument_3)}")
    print(f"Результат без функции sort(): {my_func_2(argument_1, argument_2, argument_3)}")