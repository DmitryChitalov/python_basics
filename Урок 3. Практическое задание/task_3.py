"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# Без функции sort()
def my_func(f_num, s_num, t_num):
    if f_num == s_num == t_num:
        sum_two_max = f'все числа равны: {f_num + s_num}' \
                      f' #(a+b)=(a+c)=(c+b)'
        return sum_two_max
    if f_num >= s_num and f_num >= t_num:
        sum_two_max = (f'{f_num + s_num} #(a+b)',
                       f'{f_num + t_num} #(a+c)'
                       f'')[f_num + s_num < f_num + t_num]
    else:
        sum_two_max = f'{s_num + t_num} #(b+c)'
    return sum_two_max


# Используя функцию sort()
def my_func_sort(f_num, s_num, t_num):
    if f_num == s_num == t_num:
        sum_two_max = f'все числа равны: {f_num + s_num}'
        return sum_two_max
    num_list = [f_num, s_num, t_num]
    num_list.sort(reverse=True)
    sum_two_max = num_list[0] + num_list[1]
    return sum_two_max


u_choise = 0
while u_choise != '1':
    f_ch = int(input("Введите первое число: "))
    s_ch = int(input("Введите второе число: "))
    t_ch = int(input("Введите третье число: "))
    print(f"not_sort(): Сумма наибольших введенных чисел: "
          f"{my_func(f_ch, s_ch, t_ch)}")
    print(f"    sort(): Сумма наибольших введенных чисел: "
          f"{my_func_sort(f_ch, s_ch, t_ch)}")
    u_choise = input("     QUIT : 1 ")
