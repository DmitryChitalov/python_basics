"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
#Вариант 1
def sum_max(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))
sum_max(200, 500, 400)

#Вариант 2
def sum_max(*args):
    total = list(args)
    i = 0
    result = 0
    while i != 2:
        max_num = max(total)
        result += max_num
        total.remove(max_num)
        i += 1
    print(result)
sum_max(1, 2, 3)