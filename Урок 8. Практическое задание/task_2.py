"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
#Task_2
class MyException(Exception):

    def __str__(self):
        return f"Недопустимое значение 0"

div = int(input('Введите делимое '))
control = True
while control:
    try:
        num = int(input('Введите делитель '))
        if num == 0:
            raise MyException
        print(div / num)
        print('Выход')
        control = False
    except MyException as e:
        print(e)
