"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
user_time = int(input('введите время в секундах: '))
hour = user_time // 3600
user_time = user_time - hour * 3600
minutes = user_time // 60
user_time = user_time - minutes * 60
seconds = user_time
print(f'результат: {hour}:{minutes}:{seconds}')
