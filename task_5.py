my_list = [7, 5, 3, 3, 2]
while True:
    a=input("Укажите балл")
    my_list.append(int(a))
    my_list.sort(reverse=True)
    print(my_list)
