"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
t = int(input("Введите время в секундах: "))
h = t // 3600
m = t % 3600
m = m // 60
s = t % 60


print(f"Время в формате ч:м:с - {h}:{m}:{s}")