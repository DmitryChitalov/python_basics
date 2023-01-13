# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

inp = input('Введите целое положительное число: ')
i = 0
max_value = 0

while i < len(inp):
    for el in inp:
        if int(el) > max_value:
            max_value = int(_)
        i += 1

print(max_value)
