"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

from random import randint

gen_rand = randint(5, 50)
print(f"Исходный список\n {gen_rand}")
r_list = []
for i in range(0, gen_rand):
    r_list.append(randint(1, 50))

print(f"Первоначальный список: {r_list}")

fin_list = [r_list[i + 1] for i in range(len(r_list) - 1) if r_list[i + 1] > r_list[i]]

print(f"Требуемый список с генератором: {fin_list}")

f_list = r_list
print(f"Исходный список 2:\n {f_list}")

fin2_list = []
i = 0
for i in range(1, len(f_list)):
    if f_list[i] > f_list[i - 1]:
        fin2_list.append(int(f_list[i]))

print(f"Требуемый список без генератора: {fin2_list}")
