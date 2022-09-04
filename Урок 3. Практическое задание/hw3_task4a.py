x = abs(float(input("Введите действительное положительное число X: ")))
y = -abs(int(input("Введите целое отрицательное число Y: ")))


def my_func():
    return x ** y


print(f"1 способ: X в степени Y = {my_func()}")
