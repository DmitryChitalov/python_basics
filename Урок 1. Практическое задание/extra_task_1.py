'''
Задача 2: Найдите сумму цифр трехзначного числа.

Пример:

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

number = int(input("Ведите целое положительное число: "))

sum_digit = 0

while True:
    mod = number % 10
    number //= 10

    sum_digit += mod

    if number <= 0:
        break

print(sum_digit)
