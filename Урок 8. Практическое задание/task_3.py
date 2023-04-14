"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OwnError(Exception):
    def __init__(self, value):
        try:
            isinstance(int(value), int)
            self.value = value
        except ValueError:
            print(f"{value} - не является числом")
            self.value = 0


result_list = []

while True:
    user_value = input("Введите число: ")

    if user_value == 'stop':
        break

    element = OwnError(user_value)
    if element.value == user_value:
        result_list.append(user_value)

print('Результат:', *result_list)
print('\nExit Program')






'''     
        
        try:
            int(el)
            new_list.append(el)
            raise OwnError("В списке не все данные являются числами!")
        except OwnError as err:

    print(err)



    for el in user_list:
        el = int(el)
            raise OwnError("В списке не все данные являются  числами!")
        if not isinstance(el, int):
            raise OwnError("В списке не все данные являются  числами!")
            
            result = [int, (el) for el in user_list]
            
             if el == 'stop':
            print(f"Стоп-фактор. Завершение работы программы.\n"
                  f"Результат ввода: {new_list}")
            
            
            
'''