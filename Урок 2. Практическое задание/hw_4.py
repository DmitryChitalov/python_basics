my_li = input('Введите строку: ').split()
num = 1
for elem in my_li:
    if len(elem) >= 10:
        print(f"{num} {elem[:10]}")
    else:
        print(f" {num} {elem}")
    num += 1