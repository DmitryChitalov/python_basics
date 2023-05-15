from itertools import cycle, count

for i in count(3):
    print(i)
    if i >= 10:
        break


i = 0
my_list = ['a', 'b', 'c']
for el in cycle(my_list):
    print(el)
    i += 1
    if i >= 10:
        break

