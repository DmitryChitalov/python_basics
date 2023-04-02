"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(a, b, c):
    if a + b > a + c and a + b > b + c:
        return a + b
    if a + c > a + b and a + c > b + c:
        return a + c
    if b + c > a + b and b + c > a + c:
        return b + c


try:
    n1 = int(input("a = "))
    n2 = int(input("b = "))
    n3 = int(input("c = "))
    print(f"The sum of the two maximum numbers:  {my_func(n1, n2, n3)}")
except ValueError as e:
    print(f"{e}")


