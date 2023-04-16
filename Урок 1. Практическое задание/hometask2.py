# Каждое из слов «class», «function», «method» записать в байтовом формате
# без преобразования в последовательность кодов
# не используя!!! методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

# Подсказки:
# --- b'class' - используйте маркировку b''
# --- используйте списки и циклы, не дублируйте функции

word_1 = b'class'
word_2 = b'function'
word_3 = b'method'

print(type(word_1), type(word_2), type(word_3))
print(word_1, word_2, word_3)
print(len(word_1), len(word_2), len(word_3))
