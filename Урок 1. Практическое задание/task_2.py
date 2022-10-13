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
hours = seconds / 3600.0
minutes = seconds / 60.0

print("Время в пеерсчете ч:м:с - %.1f : %.1f : %d" % (hours, minutes, seconds))

pass_hours = seconds // 3600
pass_minutes = seconds // 60 - pass_hours * 60
pass_seconds = seconds - pass_minutes * 60 - pass_hours * 3600

print(f"Время в формате ч:м:с - {pass_hours:02} : {pass_minutes:02} : {pass_seconds:02}")

