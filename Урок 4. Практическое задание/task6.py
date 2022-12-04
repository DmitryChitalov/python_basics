from itertools import islice, count, cycle
from sys import argv

#итератор, генерирующий целые числа, начиная с указанного
script_name, number = argv
print("Имя скрипта: ", script_name)
print("Начальное число: ", number)

for el in islice(count(int(number)), 5):
        print(el)

print("\n")
#итератор, повторяющий элементы некоторого списка, определённого заранее

my_list = ["sadasd", 21332, 3213, "dsf2", "dad"]
for el in islice(cycle(my_list), 5):
        print(el)