"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(a, b, c):
    list_args = [a, b, c]
    sum = max(list_args)
    list_args.remove(sum)
    sum += max(list_args)
    return sum
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
print(my_func(first, second, third))
