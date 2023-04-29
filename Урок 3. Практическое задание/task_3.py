"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(*nums):
    """
    Принимает на вход любое кол-во чисел, сортирует их в порядке убывания и складывает все элементы,
    кроме последнего.
    :param nums: Входящие элементы *args
    :return: Возвращает сумму всех элементов, кроме последнего.
    """
    nums_list = list(nums)
    for itter in range(len(nums_list)):
        for itter_2 in range(itter, len(nums_list)):
            if nums_list[itter] < nums_list[itter_2]:
                nums_list[itter], nums_list[itter_2] = nums_list[itter_2], nums_list[itter]
    nums_list.remove(nums_list[-1])
    result = sum(nums_list)
    return result


def my_func_sort(*nums):
    """
    Принимает на вход любое кол-во чисел, сортирует их в порядке убывания (sort) и складывает все элементы,
    :param nums:  Входящие элементы *args
    :return: Возвращает сумму всех элементов, кроме последнего.
    """
    nums_list = list(nums)
    nums_list.sort(reverse=True)
    nums_list.remove(nums_list[-1])
    result = sum(nums_list)
    return result


user_nums = []

while len(user_nums) != 3:
    for i_num in range(1, 3 + 1):
        try:
            user_number = float(input(f'Введите {i_num} число: '))
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз\n')
            user_nums.clear()
            break
        else:
            user_nums.append(user_number)

print(f'Без функции sort() - {my_func(user_nums[0], user_nums[1], user_nums[2])}')
print(f'C функцией sort() - {my_func_sort(user_nums[0], user_nums[1], user_nums[2])}')
