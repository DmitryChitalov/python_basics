"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time_user = int(input("Введите время в секундах: "))

result_hours = time_user // 3600
result_minutes = (time_user - result_hours * 3600) // 60
result_seconds = time_user - result_hours * 3600 - result_minutes * 60
print(f"{result_hours}:{result_minutes}:{result_seconds} (чч:мм:сс)")