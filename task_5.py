numb_sum = 0
number_str = input("Введите несколько чисел через пробел: ")
with open("numbers.txt", "w+") as file:
    file.write(number_str)
    file.seek(0)
    numbers = file.read().split()
    for el in numbers:
        numb_sum += int(el)
    print(numb_sum)