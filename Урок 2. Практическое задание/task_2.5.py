el_count = int(input("Введите количество элементов списка: "))
my_array = []
i = 0
while i < el_count:
    my_array.append(int(input("Введите следующее значение списка: ")))
    i += 1
print(my_array)
my_array.sort(reverse=True)
print(my_array)
my_num = int(input("Введите рейтинг: "))
if my_num > 0:
    my_array.append(my_num)
    my_array.sort(reverse=True)
    print(f"Новый рейтинг: {my_array}")
else:
    print("Ошибка. Вы ввели не натуральное число")
