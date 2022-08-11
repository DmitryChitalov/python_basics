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
while True:
    n = input("Введите целое положительное число: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Введите целое число")
        continue
current_index = 0
item_max = 0
str_n = str(n)
while True:
    item_n = int(str_n[current_index])
    if item_n == 9:
        item_max = item_n
        break
    if item_n > item_max:
        item_max = item_n
    current_index += 1
    if current_index > len(str_n) - 1:
        break
    else:
        continue
print(f"Самая большая цифра в числе: {item_max}")
