my_list = input("Введите целые числа через пробел: ").split()

n = len(my_list)

for i in range(0, n - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("Результат:", my_list)
