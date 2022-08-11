my_list = (input("Введите слова через пробел: ")).split()
for d, el in enumerate(my_list, 1):
    print(d, el[:10])