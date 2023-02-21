#3.7.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(string):
    words = string.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word[0].upper() + word[1:])
    return ' '.join(capitalized_words)

string = input("Введите текст в нижнем регистре: ")
print(int_func(string))