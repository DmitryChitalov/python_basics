__author__ = 'AndreiM'
__version__ = "1.0 25.03.2023"
print("\n task_3 \n -------- \n")

def my_func1(x, y, z):
    list = [x, y, z]
    list.sort()
    print(f'Сумма чисел', list[-1] + list[-2])
my_func1(float(input('\n# 1-й вариант sort() \nВведите 1-е число: ')), float(input('Введите 2-е число: ')), float(input("Введите 3-е число: ")))


def my_func(x, y, z):
    if x >= y and y >= z:
        return x + y
    elif x > y and x < z:
        return x + z
    else:
        return y + z

print(my_func(float(input('*** 2-й вариант my_func\nВведите 1-е число: ')),
              float(input('Введите 2-е число: ')),
              float(input("Введите 3-е число: "))))



"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""