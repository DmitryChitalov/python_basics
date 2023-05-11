from functools import reduce

def my_func(first_el, next_el):
    return first_el * next_el

my_list = [el for el in range(100, 1001, 2)]
result = reduce(my_func, my_list)
print(result)
