class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

new_data = (input("Введите два числа (делимое и делитель) через "
                  "пробел: ")).split()
try:
    if int(new_data[1]) == 0:
        raise OwnError("Деление на ноль не допускается")
    result = int(new_data[0]) / int(new_data[1])
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат деления равен {result}")