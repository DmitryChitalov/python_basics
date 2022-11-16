"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnDivisionByZeroError(Exception):
    """
    Собственный класс исключения с кастомным сообщением
    """
    def __init__(self, message) -> None:
        super().__init__(message)  # для хранения сообщения используем атрибуты раодителя

    @property
    def message(self):
        """
        возвращает какстомное сообщение
        """
        return self.args[0]


while True:
    user_inp = input("Введите делимое: ")
    try:
        arg_1 = int(user_inp)
    except ValueError:
        print("Делимое должно быть числом!")
    else:
        break

while True:
    user_inp = input("Введите делитель: ")
    try:
        arg_2 = int(user_inp)
    except ValueError:
        print("Делитель должен быть числом!")
    else:
        break

print(f"Результат деления {arg_1} на {arg_2}: ", end='')
try:
    if arg_2 == 0:
        raise OwnDivisionByZeroError("делитель равен 0")
    result = arg_1 / arg_2
except OwnDivisionByZeroError as e:
    print(f"Ошибка: {e.message}")
else:
    print(result)
