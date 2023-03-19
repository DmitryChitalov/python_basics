"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

#Можно конечно сделать ещё проверку на кол-во вводимых секунд, чтобы исключить кол-во часов более 23 (не более 86399 секунд)
#и проверку формата вводимых данных
seconds = int(input('Введите время в секундах: '))
if seconds // 3600 < 10:
    hour = "0"+str(seconds // 3600)
else:
    hour = seconds // 3600
if seconds % 3600 // 60 < 10:
    minute = "0"+str(seconds % 3600 // 60)
else:
    minute = seconds % 3600 // 60
if seconds % 3600 % 60 < 10:
    second = "0" + str(seconds % 3600 % 60)
else:
    second = seconds % 3600 % 60
print(f"Время - {hour}:{minute}:{second}")


import time
time_format = time.strftime("%H:%M:%S", time.gmtime(seconds))
print("Время -",time_format)
