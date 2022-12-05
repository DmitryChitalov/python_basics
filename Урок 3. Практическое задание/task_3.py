"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(nums, keys):
    """ Функция, которая принимает три позиционных аргумента """
    if keys == 1:
        nums.sort()
        nums = nums[-2::]
        return nums[0] + nums[1]
    elif keys == 2:
        new_list = []
        while nums:
            min_elem = nums[0]
            for elem in nums: 
                if elem < min_elem:
                    min_elem = elem
            new_list.append(min_elem)
            nums.remove(min_elem)
            new_list = new_list[-2::]
        return new_list[0] + new_list[1]


print(my_func([10, 40, 30], 1))
print(my_func([10, 40, 30], 2))
