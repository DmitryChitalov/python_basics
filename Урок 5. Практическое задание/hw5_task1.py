my_f = open("my_file.txt", "w", encoding='utf-8')
while True:
    my_str = input("Введите строки файла: ")
    my_f.writelines(my_str + '\n')
    if not my_str:
        break
my_f.close()
