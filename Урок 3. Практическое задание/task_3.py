"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(arg_1, arg_2, arg_3):
    arg_list = [arg_1, arg_2, arg_3]
    #Результат с применением функции сортировки
    result_list_1 = sorted(arg_list, reverse=True)[0:2]
    #Результат без функции функции сортировки
    result_list_2 = []
    for i in range(2):
        maximum = 0

        for j in range(len(arg_list)):
            if arg_list[j] > maximum:
                maximum = arg_list[j]

        arg_list.remove(maximum)
        result_list_2.append(maximum)

    return f'Вариант 1: {sum(result_list_1)}\nВариант 2: {sum(result_list_2)}'


try:
    var_1 = float(input("Число 1: "))
    var_2 = float(input("Число 2: "))
    var_3 = float(input("Число 3: "))
    print(my_func(var_1, var_2, var_3))
except ValueError:
    print("Некорректно. Введите число.")
