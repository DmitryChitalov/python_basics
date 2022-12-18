"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a, b, c):
    first_num = max(a, b, c)
    if first_num == b:
        second_num = max(a, c)
    elif first_num == a:
        second_num = max(b, c)
    elif first_num == c:
        second_num = max(a, b)
    print(f"Сумма двух наибольших чисел без sort(): {first_num + second_num}")
#another answer
#def get_max(*args):
#    lst = list(args)
#    i = 0
#    res = 0 
#    while i != 2:
#        max_val = max(lst)
#        res += max_val
#        lst.remove(max_val)
#        i += 1
#    print(res)



def sort_func(sa, sb, sc):
    res = sorted([sa, sb, sc])
    print(f"Сумма двух наибольших чисел с sort: {sum(res[1:3])}")
#or print(sum(sorted(list(args), reverse=True)[:2]))

val1 = int(input("Первое число: "))
val2 = int(input("Второе число: "))
val3 = int(input("Третье число: "))

my_func(val1, val2, val3)
sort_func(val1, val2, val3)
