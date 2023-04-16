"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class ZeroError(Exception):
    t = "Делить на ноль нельзя"

    def __str__(self):
        return self.t


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise ZeroError

        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            chisl, znam = map(Number, input("Введите делимое и делитель через пробел, затем Enter: ").split())
            print(chisl / znam)
        except ZeroError as e:
            print(e)
        except ValueError as e:
            print(e)
            break
