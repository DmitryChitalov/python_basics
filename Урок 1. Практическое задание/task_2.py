"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time_sec = int(input("Please enter time in seconds: "))
seconds = time_sec % 60
# print("seconds: ", seconds)
minutes1 = time_sec // 60
minutes = minutes1 % 60
# print("minutes: ", minutes)
hours = time_sec // 3600
# print("hours: ", hours)
print("Your time is {:0>2d}:{:0>2d}:{:0>2d}".format(hours, minutes, seconds))