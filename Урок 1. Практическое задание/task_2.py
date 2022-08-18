"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
while True:
    seconds = input("Введите время в секундах: ")
    try:
        seconds = int(seconds)
        break
    except ValueError:
        print("Введите целое число")
        continue
minutes = seconds / 60
hours = minutes / 60
print(f"Время в формате ч:м:с - {'{:.1f}'.format(hours)} : {'{:.1f}'.format(minutes)} : {str(seconds)}")