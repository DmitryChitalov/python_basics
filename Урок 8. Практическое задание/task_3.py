"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""
class ClassExcept(Exception):
    def __init__(self, data):
        self.data = data


def Check_content_list(str):
    if str.isdigit():
        return str
    else:
        try:
            float(str)
            return str
        except ValueError:
            raise ClassExcept(f"Ошибка: {str}")


numm = ""
list_num = []
print("Чтобы выйти нажмите 'q'")
print("Ввод числа по одному:")
while numm != "q":
    try:
        numm = input("- ")
        list_num.append(Check_content_list(numm))
    except ClassExcept as i:
        if numm != "q":
            print(i.data)

print(f"\nСписок: {list_num}")