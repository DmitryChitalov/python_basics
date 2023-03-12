my_list = [7, 5, 3, 3, 2]
while True:
    n = input("ВВедите оценку от 1 до 10: ")
    if n != 'q':
        my_list.append(int(n))
        my_list.sort(reverse=True)
        print(my_list)
    else:
        break
