my_list = input("Введите слова через пробел: " ).split()
n = 1
for element in my_list:
    if len(element) > 10:
        print(f"{n}. {element[:10]}")
    else:
        print(f"{n}. {element}")
    n += 1
print()
