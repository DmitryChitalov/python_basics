"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
inp = ''
data = []
while inp != 'stop':
    inp = input('Write integer to add to your list or insert stop, to finish work: ')
    try:
        data.append(int(inp))
    except OwnError as err:
        raise OwnError("Thi is not integer")
    except:
        continue
print(data)