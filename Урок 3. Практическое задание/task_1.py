"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""
def divs(first_number, second_number):
    division_operation = False
    result_divs = 0
    while not division_operation:
        try:
            result_divs = first_number / second_number
            division_operation = True
        except ZeroDivisionError:
            print("Вы что? Пытаетесь делить на 0?)) ")
            second_number = int(input("Повторно укажите делитель: "))
    return result_divs


x = int(input("Введите делимое число: "))
y = int(input("Введите делитель числа: "))
result = divs(x, y)
print(f"Ответ: ", result)