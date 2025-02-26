"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
def can_be_byte_string(word):
    try:
        eval(f"b'{word}'")
        return True
    except SyntaxError:
        return False


words = ["attribute", "класс", "функция", "type"]

for word in words:
    if not can_be_byte_string(word):
        print(f"Слово '{word}' невозможно записать в байтовом формате с помощью маркировки b''")
