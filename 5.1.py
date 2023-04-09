strings = []

while True:
    with open('task01.txt', 'a+') as f:
        string = input("Введите строку >>> ")

        if not string:
            break

        f.write(f"{string}\n")