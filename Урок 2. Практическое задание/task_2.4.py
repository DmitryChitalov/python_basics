my_array = input("Введите строку: ")
my_word = []
num = 1
for el in range(my_array.count(' ') + 1):
    my_word = my_array.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word[el]}")
        num += 1
    else:
        print(f" {num} {my_word[el][0:10]}")
        num += 1
