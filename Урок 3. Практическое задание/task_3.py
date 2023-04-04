"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func1(var1, var2, var3):
    mylist = [var1, var2, var3]
    mylist.sort()
    print("1) используя функцию sort(). Ответ:",  mylist[1] + mylist[2])


def my_func2(var1, var2, var3):
    if var1 < var2 and var1 < var3:
        print("2) без функции sort(). Ответ:", var2 + var3)
    elif var2 < var3:
        print("2) без функции sort(). Ответ:", var1 + var3)
    else:
        print("2) без функции sort(). Ответ:", var1 + var2)


my_list = []
for i in range(1, 4):
    my_list.append(int(input(f'Введите {i} число: ')))

my_func1(*my_list)
my_func2(*my_list)
