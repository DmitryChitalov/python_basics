"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

"""Высчитывает сумму чисел n + nn + nnn."""
n_number = int(input("Введите число: "))     #Запрашиваем число у пользователя
box = str(n_number)                          #Присваеваем тип данных str (строка)
var_1 = box + box
var_2 = box + box + box
answer = n_number + int(var_1) + int(var_2)
"""Расчет ответа"""
print(n_number, "+", var_1, "+", var_2, "=", answer)   #Вывод результата
