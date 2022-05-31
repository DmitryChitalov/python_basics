"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
from sys import argv
from random import randint

prog_name, gen, count = argv

my_list = []
if(gen == 'y'):
    my_list = [randint(0, 1000) for i in range(0, int(count))]
elif(gen == 'n'):
    for i in range(0, int(count)):
        my_list.append(int(input("Введите число: ")))

print(my_list)
i = 1
ret_list = []
while(i < int(count)):
    if(my_list[i - 1] < my_list[i]):
        ret_list.append(my_list[i])
    i += 1
print(ret_list)

