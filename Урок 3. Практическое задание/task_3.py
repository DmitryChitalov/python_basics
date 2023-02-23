"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func_f(f_num, s_num, t_num):
    tmp_tup = [f_num, s_num, t_num]
    tmp_tup.sort()
    return tmp_tup[1] + tmp_tup[2]


print(my_func_f(10, 20, 30))


def my_func_s(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        if num_2 >= num_3:
            rez = num_1 + num_2
        else:
            rez = num_1 + num_3
    elif num_2 >= num_1 and num_2 >= num_3:
        if num_1 >= num_3:
            rez = num_2 + num_1
        else:
            rez = num_2 + num_3
    elif num_3 >= num_1 and num_3 >= num_2:
        if num_1 >= num_2:
            rez = num_3 + num_1
        else:
            rez = num_3 + num_2
    return rez


print(my_func_s(10, 20, 30))