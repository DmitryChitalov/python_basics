# Задание 2.

# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Пример:
# Введите время в секундах: 3600
# Время в формате ч:м:с - 1.0 : 60.0 : 3600

time = int(input('Enter time in seconds'))
hours = time//3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (time % 3600) // 60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (time % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
print(f'Время в формате ч:м:с - ', hours_res, ':', minutes_res, ':', seconds_res)
