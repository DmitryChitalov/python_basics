"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генераторное выражение.
"""

my_number = 240

my_list = list(range(10, my_number + 1))

print(my_list)

new_list = [el for el in my_list if (el % 20 == 0 or el % 21 == 0)]

print('----------')
print(new_list)


