'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
class MyErrDivision(Exception):
    def __init__(self):
        self.txt = 'Попытка деления на 0'


def division():
    try:
        a = float(input('Делимое: '))
        b = float(input('Делитель: '))
        if b == 0:
            raise MyErrDivision
        print(f'a / b = {a / b: .4f}')
    except MyErrDivision as err:
        print(err.txt)


division()