"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
# Задание 2 вывод информации как в примере
seconds = int(input("Введите время в секундах: "))
if seconds > 59:
    minutes = seconds // 60
    hour = minutes // 60
print("{0} ч:{1} мин:{2} сек".format(hour, minutes, seconds))

# Задание 2 Вывод информации по времени в зависимости от секунд 2 вариант реализации
seconds_1 = int(input("Введите время в секундах: "))
if seconds_1 > 59:
    minutes_1 = seconds_1 // 60
    seconds_1 = seconds_1 - minutes_1 * 60
    if minutes_1 > 59:
        hour_1 = minutes_1 // 60
        minutes_1 = minutes_1 - hour_1 * 60
    else:
        hour_1 = 0
else:
    minutes_1 = 0
    hour_1 = 0
print("{0} ч:{1} мин:{2} сек".format(hour_1, minutes_1, seconds_1))