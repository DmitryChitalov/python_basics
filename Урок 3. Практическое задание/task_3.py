"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

<<<<<<< HEAD

=======
>>>>>>> Amendments_Homework#1,2,3
def my_func():
    """Функция для определиния суммы с использованием функции sort()"""
    arg_1 = int(input("Ввудите фргумент A =  "))
    arg_2 = int(input("Ввудите фргумент B =  "))
    arg_3 = int(input("Ввудите фргумент C =  "))
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
<<<<<<< HEAD
    summa = my_list[1] + my_list[2]
    return summa


suumma = my_func()
print(f"Результат:  {suumma} ")
=======
    result_1 = my_list[1] + my_list[2]
    return result_1


result_2 = my_func()
print(f"Результат:  {result_2} ")
>>>>>>> Amendments_Homework#1,2,3


def my_func_2():
    """Функция для определиния суммы без использованием функции sort()"""
    arg_1 = int(input("Ввудите фргумент A =  "))
    arg_2 = int(input("Ввудите фргумент B =  "))
    arg_3 = int(input("Ввудите фргумент C =  "))
    my_list = [arg_1, arg_2, arg_3]
    number_1 = 0
    for el in range(len(my_list) - 1):
        if el is number_1:
            tmp = my_list[el]
            my_list[el] = my_list[el + 1]
            my_list[el + 1] = tmp
    print(my_list)
<<<<<<< HEAD
    summa = my_list[1] + my_list[2]
    return summa


suumma = my_func_2()
print(f"Результат:  {suumma} ")
=======
    result_1 = my_list[1] + my_list[2]
    return result_1


result_2 = my_func_2()
print(f"Результат:  {result_2} ")
>>>>>>> Amendments_Homework#1,2,3
