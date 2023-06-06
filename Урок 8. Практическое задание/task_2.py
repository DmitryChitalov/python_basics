class DivisionByZeroError(Exception):
    pass

try:
    dividend = int(input("Введите делимое: "))
    divisor = int(input("Введите делитель: "))

    if divisor == 0:
        raise DivisionByZeroError("Деление на ноль запрещено")

    result = dividend / divisor
    print("Результат деления:", result)

except ValueError:
    print("Ошибка: Введите целое число")
except DivisionByZeroError as e:
    print("Ошибка:", e)
