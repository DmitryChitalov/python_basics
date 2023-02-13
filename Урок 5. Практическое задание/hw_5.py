with open("file_5.txt", "w", encoding='utf-8') as file_5:
    try:
        my_list = input("Введите числа через пробел: ")
        file_5.writelines(my_list)
        my_number = my_list.split(' ')
        print(f"Сумма чисел: {sum(map(int, my_number))}")
    except ValueError:
        print("Вводите только цифры")