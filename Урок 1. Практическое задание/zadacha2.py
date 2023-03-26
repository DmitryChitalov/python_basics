# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input())
number1 = number % 10
number2 = number // 10
number22 = number2 % 10
number3 = number // 100
result = number1 + number22 + number3
print(result)