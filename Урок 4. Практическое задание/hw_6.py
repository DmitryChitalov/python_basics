from itertools import count, cycle

for el in count(3):
    if el >10:
        break
    else:
        print(el)


cities_list = ['Saint-Petersburg', 'Moscow', 'Ekaterinburg', 'Vyborg']
c = len(cities_list)
iter = cycle(cities_list)
for el in iter:
    while c > 0:
        print(next(iter))
        c -= 1
