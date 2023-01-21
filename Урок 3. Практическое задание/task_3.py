"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# С использованием sort()
def my_func(*elem):
    print(sum(sorted(list(elem), reverse=True)[:2]))


try:
    el_1 = int(input('Введите первое число: '))
    el_2 = int(input('Введите второе число: '))
    el_3 = int(input('Введите третье число: '))
    my_func(el_1, el_2, el_3)
except ValueError:
    print("Необходимо ввести только числа!\nПереход к следующему варианту.")


# Без использвоания sort()
def my_func(*elem):
    lst = list(elem)
    i = 0
    res = 0
    while i < 2:
        el_max = max(lst)
        res += el_max
        lst.remove(el_max)
        i += 1
    print(res)

try:
    el_1 = int(input('Введите первое число: '))
    el_2 = int(input('Введите второе число: '))
    el_3 = int(input('Введите третье число: '))
    my_func(el_1, el_2, el_3)
except ValueError:
    print("Необходимо ввести только числа!\nНачните заново.")
