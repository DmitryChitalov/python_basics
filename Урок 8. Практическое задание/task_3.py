"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

# Выводим на экран задание
print('\nУрок 8 Задание 3\n')

# Объявляем класс
class IsDigit(Exception):
    def __init__(self, text):
        self.text = text

# Объявляем функцию проверки вводных данных
def check_text(in_str):
    if in_str.isnumeric():
        return in_str
    else:
        try:
            float(in_str)
            return in_str
        except ValueError:
            raise IsDigit(f'Введенное значение "{in_str}" не является числом!')

# Объявляем переменные
input_list = []
input_text = ''

# Создаем список из чисел и проверяем
while input_text != "Выход":
    input_text = input('Введите числовой элемент для создания списка из чисел("Выход" - завершение программы):\n')
    try:
        input_text = check_text(input_text)
        input_list.append(input_text)
    except IsDigit as err:
        print(err)
# Вывод результата
print(input_list)
