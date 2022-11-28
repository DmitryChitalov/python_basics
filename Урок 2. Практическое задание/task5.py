my_list = [7, 5, 3, 3, 2]
new_rating = int(input("Введите новый рейтинг: "))
i = len(my_list) - 1
if new_rating < 0:
    print("Значение должно быть положительным!")
elif new_rating > max(my_list):
    my_list.insert(0, new_rating)
else:
    my_list.append(new_rating)
    while i > 0:
        if my_list[i] < my_list[i + 1]:
            buffer = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = buffer
            i -= 1
        else:
            break
print(f"Новый рейтинг: {my_list}".format(my_list=my_list))