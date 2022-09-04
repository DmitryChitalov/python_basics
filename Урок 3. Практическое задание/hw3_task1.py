arg_1 = int(input("Введите первое число: "))
arg_2 = int(input("Введите второе число: "))
if arg_2 != 0:
    def my_div():
        return arg_1 / arg_2
    print(f"Результат: {my_div()}")
else:
    print("На ноль делить нельзя")
