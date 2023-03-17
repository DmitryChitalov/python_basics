"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
#!/usr/bin/env python3
<<<<<<< HEAD
user_input = int(input("Пожалуйста, введите продолжительность в секундах: "))

result_hours = user_input // 3600
result_minutes = (user_input - result_hours * 3600) // 60
result_seconds = user_input - result_hours * 3600 - result_minutes * 60

print(f"Мы с Питоном насчитали {user_input // 3600:02d}:{(user_input - result_hours * 3600) // 60:02d}:{user_input - result_hours * 3600 - result_minutes * 60:02d} (чч:мм:сс)")
print(f"Мы с Питоном насчитали {result_hours:02d}:{result_minutes:02d}:{result_seconds:02d} (чч:мм:сс)")
print(f"Мы с Питоном посмотрели пример и пересчитали.  {result_hours:02d}:{result_minutes:02d}:{result_seconds:02d} (чч:мм:сс)")
