# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.


my_list = [(input("Введите строку из нескольких слов > "))]
print(my_list)
i = 1

for el in my_list:
    new_list = el.split()
for el in new_list:
        length = len(el)
        if length < 11:
            print(f" {i} {el}")
            i = i + 1
        else:
            print(f" {i} {el[0:10]}")
            i = i + 1

