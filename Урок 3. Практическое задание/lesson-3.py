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
from typing import List, Any


def division(divisible, divider):
    """"функция деления"""
    try:
        rezult = divisible / divider
    except ZeroDivisionError:
        rezult = ("Некорректный делитель")
    return rezult


val_1 = int(input("Введите делимое"))
val_2 = int(input("Введите делитель"))

print(division(val_1, val_2))

"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def data(name, surname, birthday, city, email, phone):
    """функция вывода информации по пользователю"""
    print(f"{name} {surname} {birthday} года рождения проживает в городе {city}, email {email}, телефон {phone}")


val_1 = input("Введите имя")
val_2 = input("Введите фамилию")
val_3 = input("Введите год рождения")
val_4 = input("Введите город проживания")
val_5 = input("Введите email")
val_6 = input("Введите номер телефона")
data(name=val_1, surname=val_2, birthday=val_3, city=val_4, email=val_5, phone=val_6)

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_1(arg_1, arg_2, arg_3):
    """"функция для нахождения двух наибольших аргументов"""
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    summary = my_list[2] + my_list[1]
    return summary


valu_1 = int(input("Введите первый аргумент"))
valu_2 = int(input("Введите второй аргумент"))
valu_3 = int(input("Введите третий аргумент"))
print(my_func_1(valu_1, valu_2, valu_3))


def my_func_2(arg_1, arg_2, arg_3):
    """"функция для нахождения двух наибольших аргументов без сортировки"""
    summary = max(arg_1, arg_2, arg_3)
    if arg_1 == summary:
        if arg_2 >= arg_3:
            summary = summary + arg_2
        else:
            summary = summary + arg_3
    elif arg_2 == summary:
        if arg_1 >= arg_3:
            summary = summary + arg_1
        else:
            summary = summary + arg_3
    else:

        if arg_1 >= arg_2:
            summary = summary + arg_1
        else:
            summary = summary + arg_2
    return summary


valu_1 = int(input("Введите первый аргумент"))
valu_2 = int(input("Введите второй аргумент"))
valu_3 = int(input("Введите третий аргумент"))
print(my_func_2(valu_1, valu_2, valu_3))

""" Программа принимает действительное положительное число x и целое отрицательное число y.
 Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
 При решении задания нужно обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""

x = float(input('Введите действительное число х'))
y = int(input('Введите целое чило у'))


def my_func_4a(x, y):
    """"функция для возведения числа в степень"""
    rezult = x ** y
    print(rezult)


my_func_4a(x, y)


def my_func_4b(x, y):
    """"функция для возведения числа в степень без ** """
    i = 1
    rezult = x
    if y > 0:
        while i < y:
            rezult = rezult * x
            i += 1
        print(rezult)
    if y < 0:
        while i < (-y):
            rezult = rezult * x
            i += 1
        all_rezult = 1 / rezult
        print(all_rezult)

    if y == 0:
        rezult = 1
        print(rezult)


my_func_4b(x, y)

"""5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, 
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме 
 и после этого завершить программу"""


def func_for_summ(my_sum):
    """"функция для нахождения суммы последовательностей"""
    my_list = input("Введите числа через пробел").split()
    for i in range(len(my_list)):
        if my_list[i] != "/":
            my_sum = my_sum + int(my_list[i])
        if my_list[i] == "/":
            print(my_sum)
            exit("завершение программы")
    print(my_sum)
    func_for_summ(my_sum)


func_for_summ(0)

""" Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""


def int_func(text_list):
    """"функция для преобразования каждого слова строки из строчной в заглавную"""
    new_text = text_list.title()
    print(new_text)


text_list = input("Введите текст")
int_func(text_list)
