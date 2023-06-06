class OnlyNumbersError(Exception):
    pass

numbers = []
while True:
    try:
        user_input = input("Введите число (для остановки введите 'stop'): ")
        if user_input == "stop":
            break

        number = float(user_input)
        if not number.is_integer():
            raise OnlyNumbersError("Допускаются только целые числа")
        numbers.append(int(number))

    except ValueError:
        print("Ошибка: Введите число")
    except OnlyNumbersError as e:
        print("Ошибка:", e)

print("Список чисел:", numbers)
