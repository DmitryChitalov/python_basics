"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def new_func(number_1, number_2):
    return number_1 / number_2


try:
    answer = new_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")))
    print(answer)
except ZeroDivisionError:
    print("На ноль делить нельзя")

"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
"""


def users(name, last_name, year, city, email, phone):
    return f"{last_name} {name}, {year} г.р., город проживания - {city}, email: {email}, телефон: {phone}"


print(users(name="Надежда", last_name="Субботина", year="1994", city="Москва",
            email="nadya1994@mail.ru", phone="89042335078"))

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента 
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    if arg_1 > arg_2 or arg_1 > arg_3:
        if arg_2 > arg_3:
            return arg_1 + arg_2
        else:
            return arg_1 + arg_3
    else:
        return arg_2 + arg_3


answer_3 = my_func(1, 5, 4)
print(answer_3)

"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
"""


def my_func_1(x,y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(my_func_1(3, -5))

"""
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел 
к полученной ранее сумме и после этого завершить программу.
"""


def my_sum():
    sum_res = 0
    ex = False
    while not ex:
        number = input("Введите числа через пробел или Q для выхода - ").split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Промежуточная сумма: {sum_res}")
    print(f"Итоговая сумма: {sum_res}")


my_sum()

"""
6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
"""


def int_func(*args):
    my_str = input("Введите через пробел слова из маленьких латинских букв: ").title()
    return my_str


print(int_func())
