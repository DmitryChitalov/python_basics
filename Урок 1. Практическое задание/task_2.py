"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

print('Пожалуйста, введите время в секундах:')
s = int(input())  # считываем строку, переводим в int и кладём её в переменную
print(s)
print(f"Время в формате ч:м:с {round(s / 3600, 2)} : {round(s / 60, 2)} : {s}")
