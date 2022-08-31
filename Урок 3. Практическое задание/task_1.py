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
# """
def division (a1, a2):
    try:
        a1, a2 = int(a1), int(a2)
        division_num = a1 / a2
    except ValueError:
        return "Не корректно введены данные"
    except ZeroDivisionError:
        return  "Делить на 0 нельзя"
    return round(division_num)

print(division(input("Введите первое число: "), input("Введите второе число: ")))
