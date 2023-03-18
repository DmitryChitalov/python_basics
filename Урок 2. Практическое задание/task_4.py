"""

4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()

"""

def my_func_1(arg1, arg2, arg3):
    arg = [arg1, arg2, arg3]
    arg.sort()
    print(f'Используя функицю sort = {arg[1] + arg[2]}')

def my_func_2(arg1, arg2, arg3):
    arg = [arg1, arg2, arg3]
    sum = 0
    for element in arg:
        sum += element
    print(f'Не используя функицю sort = '
          f'{sum - min(arg)}')


arg1 = int(input('Введите аргумент 1: '))
arg2 = int(input('Введите аргумент 2: '))
arg3 = int(input('Введите аргумент 3: '))

print(f'Сумма двух наибольших значений :')
my_func_1(arg1, arg2, arg3)
my_func_2(arg1, arg2, arg3)
