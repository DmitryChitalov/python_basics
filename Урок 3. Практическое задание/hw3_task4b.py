x = abs(float(input("Введите действительное положительное число X: ")))
y = -abs(int(input("Введите целое отрицательное число Y: ")))

res = 1
for i in range(y * (-1)):
    res *= (1 / x)


print(f"2 способ: X в степени Y = {res}")
