"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

#варианты без генератора

#1-ый
new_list = []
i1 = 0
i2 = 1
while i2 <  len(my_list):
    if my_list[i1] < my_list[i2]:
        new_list.append(my_list[i2])
    i1, i2 = i1 + 1, i2 + 1
print(new_list)

#2-ой
new_list = []
a = 0
for el in my_list[1:]:
    if el > my_list[a]:
        new_list.append(el)
    a += 1
print(new_list)

#3-й
new_list = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])
print(new_list)

#Вариант с генератором
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)
