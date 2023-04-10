"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = ["Class", "Function", "Method"]

for elem in words:
    element = bytes(f"{elem}", encoding="ascii")
    print(f'{element} = {type(element)}')


