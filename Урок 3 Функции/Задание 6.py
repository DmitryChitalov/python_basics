"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


"""
Первый вариант
Работает как для одного слова (1 часть задания), так и для списка слов через пробел используя написанную 
раннее функцию (2 часть задания).
"""


def int_func(words):
    while words != words.lower():                               # проверка на ввод маленьких букв
        words = input('Enter data in small case letters: ')
    return words.title()


print(int_func(input('Enter word or words with space: ')))


"""
Второй вариант 
без title и с явным дополнением, и использованием
написанной раннее функции (для первой части задания)
"""


def int_func(wr):
    while wr != wr.lower():                                     # проверка на ввод маленьких букв
        wr = input('Enter word in small case letters: ')
    if len(wr) > 1:                                             # если список слов через пробел
        lstwr = wr.split()
        for i in range(len(lstwr)):
            startswithlst = lstwr[i][0].capitalize()
            lstwr[i] = startswithlst + lstwr[i][1::]
        return ' '.join(lstwr)
    # если одно слово
    startswith = wr[0].title()
    return startswith + wr[1::]


print(
    f'Your word is: "Paraparapam\nTadam" -----> {int_func(input("Enter word or words: "))}\nApplause please )))')
# Атмосфера шоу )))
