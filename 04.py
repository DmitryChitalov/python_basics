#Четвертое задание
x = int(input("Введите число:"))
maximum = 0
while x!=0:
    lastd = x % 10
    if lastd > maximum:
        maximum = lastd
    x = x // 10
print(maximum)