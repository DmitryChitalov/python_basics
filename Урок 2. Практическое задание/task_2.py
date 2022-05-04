str_1 = (list(input("Введите цифры: ")))
str_1[:-1:2], str_1[1::2] = str_1[1::2], str_1[:-1:2]
print(' '.join(str_1))
