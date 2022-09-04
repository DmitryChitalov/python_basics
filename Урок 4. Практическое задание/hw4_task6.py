from itertools import count
from itertools import cycle

# а) итератор, генерирующий целые числа, начиная с указанного (с 3 до 10)

for el in count(3):
    if el > 10:
        break
    else:
        print(int(el))

# б) итератор, повторяющий элементы некоторого списка, определенного заранее (ограничение: 5 элементов)

my_list = [1, 2, 3, 4, 5, 6, 7]
it = cycle(my_list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# ИЛИ

my_list = [1, 2, 3, 4, 5, 6, 7]
c = 0
for el in cycle(my_list):
    if c > 4:
        break
    print(el)
    c += 1
