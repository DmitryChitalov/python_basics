"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivOwn(Exception):
    def __init__(self, text):
        self.text = text


try:
    base_value = 10
    input_value = int(input("Введите число: "))

    if input_value == 0:
        raise ZeroDivOwn("Деление на ноль невозможно")
    else:
        out_value = base_value / input_value

except ZeroDivOwn as e:
    print(e)

except ValueError as e:
    print(f"В делении участвует не число: {e}")
else:
    print(f"Результат деления: {out_value}")
