"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))


my_func(int(input("Первое число: ")), int(input("Второе число: ")), int(input("Третье число: ")))

#Первое решение

def my_func(*args):
    args_ls = list(args)
    args_ls.remove(min(args_ls))
    print(sum(args_ls))


my_func(int(input("Первое число: ")), int(input("Второе число: ")), int(input("Третье число: ")))

#Второе решение
