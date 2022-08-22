"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# 1) используя функцию sort()

def my_func():
    count = 1
    mass = []
    while count != 4:
        arg_ = int(input(f"Введите {count} число: "))
        mass.append(arg_)
        count += 1
    mass.sort(reverse=True)
    del mass[-1]
    result = sum(mass)
    return print(f"Результат сложения наибольших чисел с использованием функции 'sort': {result}")


my_func()


# 2) без функции sort()

def my_func_nosort(arg_1, arg_2, arg_3):
    print(f"Сумма двух наибольших аргументов без использования \n"
          f"функции 'sort 'равна: {arg_1 + arg_2 + arg_3 - min([arg_1, arg_2, arg_3])}")


my_func_nosort(
    int(input("Введите первое число: ")),
    int(input("Введите второе число: ")),
    int(input("Введите третье число: "))
)
