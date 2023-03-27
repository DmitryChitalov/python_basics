new_lst = input("Введите слова черрез пробел:").split()
n = 1
for el in new_lst:
    if len(el) > 10:
        print(f"{n}. {el[:10]}")
    else:
        print(f"{n}.{el}")
        n += 1
print()
