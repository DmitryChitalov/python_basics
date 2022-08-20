my_list = input("Введите слова через пробел: ").split(' ')
for ind, el in enumerate(my_list, 1):
    print(f"{ind}) {el[:10]}")
