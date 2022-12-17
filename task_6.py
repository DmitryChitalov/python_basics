# первое задание

from itertools import count

number = int(input("Введите целое число: "))
for el in count(number):
    if el > 11:
        break
    print(el)

# второе задание

from itertools import cycle

my_list = ['Paris', 'London', 'Moscow', 'Istanbul']
i = 0
for el in cycle(my_list):
    if i > 10:
        break
    print(el)
    i += 1