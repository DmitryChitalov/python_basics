"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a, b, c):
    if a > b > c:
        return a + b
    elif a > b < c:
        return a + c
    else:
        return b + c


print(f"Сумма двух наибольших чисел: "
      f"{my_func(int(input('Введите 1-e число: ')), int(input('Введите 2-е число: ')), int(input('Введите 3-е число: ')))}")


# sort
def my_func(a, b, c):
    num_list = [a, b, c]
    num_list.sort()
    return sum(num_list[1:])


print(f"Сумма двух наибольших чисел: "
      f"{my_func(int(input('Введите 1-e число: ')), int(input('Введите 2-е число: ')), int(input('Введите 3-е число: ')))}")
