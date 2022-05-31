my_list = [7, 5, 3, 3, 2]
print("Существующий рейтинг:", my_list)
new_el = int(input('Введите новый элемент рейтинга: '))
my_list.append(new_el)
my_list.sort(reverse=True)
print(my_list)
