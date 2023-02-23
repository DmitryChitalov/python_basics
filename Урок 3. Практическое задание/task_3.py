"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(a, b, c):
    nums = [a, b, c]
    nums.sort()
    return nums[1] + nums[2]

result = my_func(3, 7, 2)
print(result)  # Output: 10


def my_func(a, b, c):
    if a >= b and a >= c:
        return a + max(b, c)
    elif b >= a and b >= c:
        return b + max(a, c)
    else:
        return c + max(a, b)

result = my_func(3, 7, 2)
print(result)  # Output: 10
