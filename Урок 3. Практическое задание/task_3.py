"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a, b, c):
    sequence = [a, b, c]
    summary_sec = []
    max_1 = max(sequence)
    summary_sec.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    summary_sec.append(max_2)
    print(sum(summary_sec))


my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
        int(input("Введите третье число: ")))
