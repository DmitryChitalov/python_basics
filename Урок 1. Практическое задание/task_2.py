"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time_in_sec = int(input("Введите время в секундах: "))

time_in_hours = time_in_sec // 3600
time_in_minutes = (time_in_sec - time_in_hours * 3600) // 60
time_in_minutes_2 = (time_in_sec) // 60
time_in_seconds = time_in_sec % 60

print('Время в общепринятом формате: %02d:%02d:%02d' % (time_in_hours, time_in_minutes, time_in_seconds))
print('Время в формате ДЗ: %.1f : %.1f : %d' % (time_in_hours, time_in_minutes_2, time_in_sec))