def my_func():
    result = 0
    q = True
    while q == True:
        number = input().split()
        buffer = 0
        for el in range(len(number)):
            if number[el] != "q":
                buffer = buffer + int(number[el])
            else:
                q = False
                break
        result = result + buffer
        print(f"Сумма: {result}")

print("Вводите числа через пробел или q - для выхода: ")
my_func()

