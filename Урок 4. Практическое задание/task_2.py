"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

Входные данные:
4 (число кустов)
1 2 3 4 (количество ягод на каждом кусте)
Выходные данные:
9
"""

from random import randint
var_n = int(input("Введите число кустов: "))
list_berry = []
for i in range(var_n):
    list_berry.append(int(input(f"Введите число ягод на {i + 1} кусте: ")))
print(list_berry)
sum_berry = [sum(list_berry[i:i+3]) for i in range(len(list_berry))]
print(sum_berry)
max_berry = max(sum_berry)
print(f"Наибольшее число:", max_berry)
