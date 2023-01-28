"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
 У пользователя нужно запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

initial_number_of_natural_numbers = int(input("введите начальное количество натуральных чисел : "))
rating_list = []
for i in range(initial_number_of_natural_numbers):
    new_element = int(input("Для изначального заполнения массива введите новый элемент массива : "))
    rating_list.append(new_element)
print(f"Начальный набор натуральных чисел выглядит так: {rating_list}")
rating_new_element = int(input("Введите новый элемент рейтинга: "))
for index in range(len(rating_list) - 1):
    if rating_list[index] == rating_new_element:
        if rating_new_element > rating_list[index + 1]:
            rating_list_new = rating_list[:index + 1] + [rating_new_element] + rating_list[index + 1:]
    elif rating_new_element > rating_list[0]:
        rating_list_new = [rating_new_element] + rating_list
    elif rating_list[index] > rating_new_element:
        if rating_list[index + 1] < rating_new_element:
            rating_list_new = rating_list[:index + 1] + [rating_new_element] + rating_list[index + 1:]
        elif rating_list[index + 1] == rating_new_element:
            rating_list_new = rating_list[:index + 1] + [rating_new_element] + rating_list[index + 1:]
        else:
            rating_list_new = rating_list + [rating_new_element]
print(rating_list_new)
