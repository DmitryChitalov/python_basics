str_list = input("Введите данные, разделенные пробелом: ").split()
print(str_list)
with open("new_file.txt", "w") as file:
    file.writelines("%s\n" % line for line in str_list)