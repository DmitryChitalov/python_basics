from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(my_list)
print(reduce(lambda a, b: a * b, my_list))
