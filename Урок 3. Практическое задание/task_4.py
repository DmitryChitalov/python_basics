"""
4. Программа принимает действительное положительное число x
и целое отрицательное число y. Выполните возведение числа x в степень y.
 Задание реализуйте в виде функции my_func(x, y).
 При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    intermediate_result = 1
    for i in range(abs(y)):
        intermediate_result = intermediate_result * x
    return 1 / intermediate_result


valid_positive_number = int(input("Введите действительное положительное число x: "))
negative_integer = int(input("Введите целое отрицательное число y: "))

print(f"Результат возведение числа x в степень y равен :{my_func_1(valid_positive_number, negative_integer)}")
print(f"Результат возведение числа x в степень y равен :{my_func_2(valid_positive_number, negative_integer)}")
