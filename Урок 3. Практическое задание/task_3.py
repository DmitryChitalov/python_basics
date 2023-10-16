"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(arg1, arg2, arg3):
    nums = [arg1, arg2, arg3]
    nums.sort()
    return nums[1] + nums[2]


def my_func(arg1, arg2, arg3):
    max1 = max(arg1, arg2, arg3)
    nums = [arg1, arg2, arg3]
    nums.remove(max1)
    max2 = max(nums)
    return max1 + max2
