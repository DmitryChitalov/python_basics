"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(word):
    """Принимает слово и возвращает его с заглавной первой буквой"""
    return word.capitalize()

def capitalize_sentence(sentence):
    """Принимает предложение и возвращает его, сделав первую букву каждого слова заглавной"""
    words = sentence.split()
    capitalized_words = [int_func(word) for word in words]
    capitalized_sentence = ' '.join(capitalized_words)
    return capitalized_sentence

# Пример использования
sentence = 'hello world, how are you?'
capitalized_sentence = capitalize_sentence(sentence)
print(capitalized_sentence)  # 'Hello World, How Are You?'
