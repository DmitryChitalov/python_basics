"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

my_string = input("Введите произвольные значения через пробел: ")
separator = " "
convert_string = my_string.split(separator)
length = len(convert_string)
for x in range(length // 2):
    even = 2 * x
    odd = 2 * x + 1
    convert_string[even:odd + 1] = [convert_string[odd], convert_string[even]]
print(separator.join(convert_string))
