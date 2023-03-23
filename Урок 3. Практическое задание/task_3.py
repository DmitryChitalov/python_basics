"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func_with_sort(*args):
    if len(args) > 1:
        args_list = []
        for el in args:
            args_list.append(el)
        args_list.sort(reverse=True)
        print("summ = ", args_list[0] + args_list[1] )
    else:
        print("only one param")

def my_func_without_sort(*args):
    if len(args) > 1:
        my_list = list(args)
        first_num = max(args, key = lambda i: int(i))
        my_list.remove(first_num)
        second_num = max(my_list, key = lambda i: int(i))
        print("summ = ", first_num + second_num)
    else:
        print("only one param")
my_func_without_sort(3, 4, 2)