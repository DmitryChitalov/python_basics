# цикл # округление до 2 знаков
a = int(input("Начальное значение км: "))
b = int(input("Конечное значение км: "))
day = 1

while a < b:
    a = a*1.1
    print(round(a, 2))
    day += 1

print("На вот такой день: ", day)
