"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class ExcLiter(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


def num_list():
    if __name__ == '__main__':
        my_list = []

        while True:
            print(f'Для завершения программы введите q')
            el = input("Введите число: ")

            if el == "q":
                break

            try:
                if not el.isdecimal():
                    raise ExcLiter(f"'{el}' вы ввели не число!")

                my_list.append(int(el))
            except ExcLiter as error:
                print(error)

        print(f'Результат: {my_list}')


num_list()
