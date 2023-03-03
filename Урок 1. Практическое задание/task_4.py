number = int(input("Введите целое число: "))
number_max = 0
while number > 0:
    number_last = number % 10
    number = number // 10
    if number_last > number_max:
        number_max = number_last
print(number_max)
