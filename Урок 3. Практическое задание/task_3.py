"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(a, b, c):
    """
        принимает три позиционных аргумента,
        и возвращает сумму наибольших двух аргументов.
        (number, number, number) -> number
        >>> my_func(10, 2, 3)
        13
        """
    nums = [a, b, c]
    first_max_num = max(nums)
    nums.remove(first_max_num)
    second_max_num = max(nums)
    return first_max_num + second_max_num

##print(my_func(11, 10, 8))

def my_func2(a, b, c):
    """
        принимает три позиционных аргумента,
        и возвращает сумму наибольших двух аргументов.
        (number, number, number) -> number
        >>> my_func(10, 2, 3)
        13
        """
    nums = [a, b, c]
    nums.sort()
    return nums[1] + nums[2]

print(my_func2(2, 15, 7))
