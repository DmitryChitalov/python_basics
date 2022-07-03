"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def num_max(*numargs):
    print(f'C используя функцию sort:', (sum(sorted(list(numargs), reverse=True)[:2])))
num_max(50, 10, 100)


def num_max(num_1, num_2, num_3):
    a = [num_1, num_2, num_3]
    b = list(filter(lambda x: x != max(a), a))
    return max(a) + max(b)
print(f'Без функции sort:', (num_max(50, 10, 100)))
