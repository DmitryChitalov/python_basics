class DivisionByZeroError(Exception):
    def __init__(self, message="Деление на ноль!"):
        self.message = message
        super().__init__(self.message)


while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if b == 0:
            raise DivisionByZeroError()
        result = a / b
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка ввода! Необходимо ввести целое число.")
    except DivisionByZeroError as e:
        print(e)
    else:
        break

