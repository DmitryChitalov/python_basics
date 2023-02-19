def int_func(*my_words):
    my_words = str(my_words)
    print(my_words.title())
    return
int_func(str(input('Введите слова через пробел: ')).split(" "))
