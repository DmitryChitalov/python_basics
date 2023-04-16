# Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

# Подсказки:
# --- используйте списки и циклы, не дублируйте функции
# --- обязательно!!! усложните задачу, "отловив" исключение,
# придумайте как это сделать


word_1 = b'attribute'
word_2 = b'класс'
word_3 = b'функция'
word_4 = b'type'   

# На кириллицу вылетает исключение:
# SyntaxError: bytes can only contain ASCII literal characters

# Пример через encode

# list_1 = ['attribute','класс','функция','type']
# for i in list_1:
#     try:
#         print(i, type(i), i.encode('ASCII'), ' - запись прошла успешно')
#     except:
#         print(i, type(i), '- невозможно преобразовать в байты')
