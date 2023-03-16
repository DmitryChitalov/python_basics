def divide_numbers():
    try:
        dividend = float(input("Введите делимое число: "))
        divisor = float(input("Введите делитель: "))
        result = dividend / divisor
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно")


divide_numbers()
