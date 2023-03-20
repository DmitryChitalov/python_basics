from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el)  # внимание - беконечный цикл!

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el)  # внимание - беконечный цикл!
