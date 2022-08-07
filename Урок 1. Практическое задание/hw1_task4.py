n = int(input("Введите целое положительное число: "))
result = n % 10
while n > 0:
    n = n // 10
    if n % 10 > result:
        result = n % 10
print("Максимальная цифра в числе: ", result)
