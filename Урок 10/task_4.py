"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ["Разработка", "Администрирование", "Protocol", "Standard"]
words_encode = []

for elem in words:
    words_encode.append(elem.encode('utf-8'))

print(f"Элементы из байтового представления ")
for elem in words_encode:
    not_bytes = elem.decode('utf-8')
    print(not_bytes, type(not_bytes))
