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

minutes = seconds / 60
hours = seconds / 3600

print(f"Получите время в формате ч:м:с - {hours:.2f}:{minutes:.2f}:{seconds}")