def delenie (a, b):
        try:
                c = a / b
                return c
        except ZeroDivisionError:
                return "деление на 0 невозможно"


print(delenie(float(input("введите делимое ")), float(input("введите делитель "))))