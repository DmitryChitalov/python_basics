"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ["разработка", "администрирование", "protocol", "standard"]

encoded_words = []
decoded_words = []

# Кодирование слов в байтовый формат
for word in words:
    encoded_word = word.encode("utf-8")
    encoded_words.append(encoded_word)

# Декодирование слов обратно в строковый формат
for encoded_word in encoded_words:
    decoded_word = encoded_word.decode("utf-8")
    decoded_words.append(decoded_word)

# Вывод результатов
for i, word in enumerate(words):
    print(f"Исходное слово: {word}")
    print(f"Байтовое представление: {encoded_words[i]}")
    print(f"Декодированное слово: {decoded_words[i]}\n")
