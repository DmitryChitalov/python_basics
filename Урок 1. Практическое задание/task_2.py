"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time = int(input("Введите время в секундах"))
hours = time // 3600
mine = (time - hours * 3600) // 60
sec = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {mine} : {sec}")
