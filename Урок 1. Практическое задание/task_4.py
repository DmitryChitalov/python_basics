# tack_4

n = int(input("Введите целое положительное число "))
max1 = n % 10
print(max1)
while n >= 1:
    n = n // 10
    print(n)
    if n % 10 > max1:
        print(n)
        print(max1)
        max1 = n % 10
        print(max1)
    elif n > 9:
        pass
print("Максимальное цифра в числе ", max1)
