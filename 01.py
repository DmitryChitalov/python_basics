a = input("Введите значения для списка:").split()
a[:-1:2], a[1::2] = a[1::2], a[:-1:2]
print(*a)
new_list = " ".join(a)
print(new_list)


