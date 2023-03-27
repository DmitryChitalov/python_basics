__author__ = 'AndreiM'
__version__ = "1.0 25.03.2023"
print("\n task_1 \n -------- \n")

def f_division (x, y):
    try:
        z = x / y
    except ZeroDivisionError as _Error:
        print(f"Вы что? Пытаетесь делить на 0!\n{_Error}")
    else:
        print(f"Деление {x}/{y} = {round(z, 2)}")

print(f_division(float(input("Введите первое число: ")), float(input("Введите второе число: "))))


"""
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