"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

my_list = []
end_of_list = 'y'

# вводим вручную элементы списка пока пользователь подтверждает продолжение ввода (y = yes)
while end_of_list == 'y':
    print("Введите тип данных нового элемента списка (1-int, 2-float, 3-bool, 4-str, 5-NoneType)")
    var_type = int(input())
    if var_type == 1:
        my_list.append(int(input("Введите новый элемент списка:")))
    elif var_type == 2:
        my_list.append(float(input("Введите новый элемент списка:")))
    elif var_type == 3:
        my_list.append(bool(input("Введите новый элемент списка:")))
    elif var_type == 4:
        my_list.append(input("Введите новый элемент списка:"))
    elif var_type == 5:
        my_list.append(None)
    else:
        print("Введен недопустимый тип данных")
    end_of_list = input("Если хотите продолжить ввод элементов, введите 'y', иначе - любое другое значение")
print(my_list)

for el in my_list:
    print(type(el))
