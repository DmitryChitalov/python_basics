"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def sort(a, b, c):
    return sum(sorted([a, b, c], reverse=True)[:2])
def no_sort(a, b, c):
    return max([a + b, a + c, b + c])
x, y, z = 7, 8, 15
print(f"используя sort(): {sort(x, y, z)}, "
      f"без sort(): {no_sort(x, y, z)}")
