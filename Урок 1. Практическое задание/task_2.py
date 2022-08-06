"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

seconds = int(input("Введите время в секундах: "))
hour = int(seconds / 3600)
my_hour = round(seconds / 3600, 1)
minute = int((seconds - hour * 3600) / 60)
my_minute = round(seconds / 60, 1)
sec = int(seconds - hour * 3600 - minute * 60)

print(f"Время в формате ч:м:с -  {my_hour} : {my_minute} : {seconds}")
print(f"Время в формате чч:мм:сс -  {hour} : {minute} : {sec}")
