"""
7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
"""


def int_func(arg1):
    """
    Функция прнинимает слово и преобразует первую букву слова в верхний регистр.
    """
    return arg1.capitalize()


offer_for_conversion = input('Введите предложение для преобразования: ')

list_of_words = offer_for_conversion.split(" ")
list_of_new_words = []
for word in list_of_words:
    list_of_new_words.append(int_func(word))
print(" ".join(list_of_new_words))
