class MyErrorZero(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = int(input("Введите число: "))
divider = int(input("Введите делитель: "))

try:
    if divider == 0:
        raise MyErrorZero("Деление на ноль!")

    result = inp_data / divider
except MyErrorZero as err:
    print(err)
else:
    print(f"Результат деления: {result}")

