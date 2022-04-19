from functools import reduce

my_string = [el for el in range(100, 1001)]
new_string = [el for el in my_string if el % 2 == 0]
rez = reduce(lambda x, y: x * y, new_string)
print(rez)
