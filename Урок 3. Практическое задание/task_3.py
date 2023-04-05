"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# 1ый способ -  используя функцию sort()
def my_func(*args):
    my_list = sorted(list(args))
    return my_list[1] + my_list[2]
   
print(my_func(10, 3, 2))

# 2ый способ - без функции sort()
def my_func(*args):
    i, amount = 0, 0
    my_list = list(args)
    while i < 2:
        amount += max(my_list)
        my_list.remove(max(my_list))
        i += 1
    return amount

print(my_func(10, 3, 2))



