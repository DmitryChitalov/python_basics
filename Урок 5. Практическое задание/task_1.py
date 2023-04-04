my_f = open("lesson4task1.txt", "w", encoding="utf-8")
while True:
    str_list = input("Ввведите данные: ")
    if str_list == "":
        break
    my_f.writelines(str_list + "\n")
my_f.close()


with open("lesson4task1.txt", "r", encoding="utf-8") as my_f:
    print(my_f.read())
