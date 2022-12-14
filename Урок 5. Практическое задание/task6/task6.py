my_f = open("task6.txt", "r", encoding='utf-8')
my_dict = {}
buffer_count = ""
content = my_f.readline()
while content != "":
    buffer = content.split()
    amount = 0
    for el in range(1, 4):
        if buffer[el] != "-":
            buffer_str = buffer[el]
            for i in range(len(buffer[el])):
                if buffer_str[i] != "(":
                    buffer_count += buffer_str[i]
                else:
                    break
            amount += int(buffer_count)
            buffer_count = ""
    buffer[0] = buffer[0][:-1]
    my_dict[buffer[0]] = amount
    content = my_f.readline()
my_f.close()
print(my_dict)