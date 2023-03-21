"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func_with_sort(arg1, arg2, arg3):
    args = [arg1, arg2, arg3]
    args.sort(reverse=True)
    print(f"Сумма двух наибольших аргументов равна: {args[0] + args[1]}")

def my_func_without_sort(arg1, arg2, arg3):
    args = [arg1, arg2, arg3]
    print(f"Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min(args)}")

while True:
    control = input("Посмотреть результат вывода функции с сортировой? (y/n): ")
    if control in {"Y", "y"}:
        my_func_with_sort(int(input("Введите аргумент 1: ")), int(input("Введите аргумент 2: ")), int(input("Введите аргумент 3: ")))
    elif control in {"N", "n"}:
        my_func_without_sort(int(input("Введите аргумент 1: ")), int(input("Введите аргумент 2: ")), int(input("Введите аргумент 3: ")))
    else:
        break
