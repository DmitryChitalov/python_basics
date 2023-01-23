"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
Пример:
для списка [5, "string", 0.15, True, None]
результат
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

type_list = [777, None, -30, 'True', True, "Hallo Welt", {"книги": "Бесы", "автор": "Достоевский Ф.М."}, 9.5]

def my_type(element):
    for element in range(len(type_list)):
print(type(type_list[element]))
   

    
