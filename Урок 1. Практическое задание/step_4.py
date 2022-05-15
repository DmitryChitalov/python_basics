# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

x = int(input("Введите число: "))
minimum, maximum = 9, 0

while x:
    x, n = divmod(x, 10)
    minimum = min(minimum, n)
    maximum = max(maximum, n)

print(f"Мин = {minimum}, Макс = {maximum}")
