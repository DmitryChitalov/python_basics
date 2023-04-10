class NonNumberListValueException(Exception):
    pass


def append_number(number_list: list):
    value = input("Введите число >>> ")

    try:
        number_list.append(float(value))
    except ValueError:
        raise NonNumberListValueException(f"Вы ввели '{value}' вместо числа")

numbers = []

while True:
    try:
        append_number(numbers)
    except NonNumberListValueException as exception:
        print(exception)
    except KeyboardInterrupt:
        print(f"\nСписок чисел = {numbers}")

        break