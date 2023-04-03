"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

list_words = ['разработка', 'администрирование', 'protocol', 'standard']

for el in list_words:
    in_bytes = el.encode('utf-8')
    print(f'тип переменной: {type(in_bytes)}, содержание:  {in_bytes}')

    in_str = in_bytes.decode('utf-8')
    print(f'тип переменной: {type(in_str)}, содержание:  {in_str}', '\n')