number = int(input('Введите целое положительное число: '))
a = number % 10
number = number // 10
while number > 0:
    if number % 10 > a:
        a = number % 10
    number = number // 10
print(a)