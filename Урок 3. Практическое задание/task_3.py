"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func (figure_1, figure_2, figure_3):
    print(
        f'Сумма двух наибольших аргументов равна: {figure_1 + figure_2 + figure_3 - min([figure_1, figure_2, figure_3])}'
        )
my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:'))
)
