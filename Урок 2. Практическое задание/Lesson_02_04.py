"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове."""
my_strc = input("введите предложение ")
my_wrd = []
number = 1
for element in range(my_strc.count(' ') + 1):
    my_word = my_strc.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word[element]}")
        number += 1
    else:
        print(f" {number} {my_word[element][0:10]}")
        number += 1
