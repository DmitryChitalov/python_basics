"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
#Вариант 1
def my_func(*var):
    print(sum(sorted(list(var), reverse=True)[:2]))
#Вариант 2
#def my_func(x, y, z):
#    sequence = [x, y, z]
#    total = []
#    max_1 = max(sequence)
#    total.append(max_1)
#    sequence.remove(max_1)
#    max_2 = max(sequence)
#    total.append(max_2)
#    print(sum(total))
my_func(100, 1, 200)