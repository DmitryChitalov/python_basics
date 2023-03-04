my_list = ['Hello\n', 'Chao\n', 'Hola\n']
with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")
