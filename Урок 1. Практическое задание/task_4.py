"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
print("Задание №4")
maxcheslo = int(input("Введите число "))
delit = 10
cheslo1 = 0
while maxcheslo > 0:
    cheslo = int(maxcheslo % delit)
    maxcheslo = int((maxcheslo - cheslo) / delit)
    if cheslo >= cheslo1:
        cheslo1 = cheslo
print(f"{cheslo1}")
