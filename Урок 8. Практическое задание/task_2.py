"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


delimoe = ""

while delimoe != "q":
    delimoe = input("Введите делимое (или q для выхода из цикла): ")
    try:
        delimoe = int(delimoe)
    except ValueError:
        if delimoe != "q":
            print("Вы ввели не число в качестве делимого. \n")
    else:
        delitel = input("Введите делитель: ")
        try:
            delitel = int(delitel)
            if delitel == 0:
                raise OwnError("Вы ввели нуль в качестве делителя! \n")
        except ValueError:
            print("Вы ввели не число \n")
        except OwnError as err:
            print(err)
        else:
            print(f"Результат деления:{delimoe / delitel} \n")
