"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
user_time = int(input("Введите время в секундах:"))
t_minutes = user_time // 60
t_hours = user_time // 3600
print(f"Время в формате ч:м:с - {t_hours},: {t_minutes},: {user_time}")
