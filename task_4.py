my_list = ['Один', 'Два', 'Три', 'Четыре']
i = 0
with open("new_file.txt") as file_1, open ("next_file", "w+",
                                           encoding="utf-8") as file_2:
    for line in file_1:
        any_line = line.split()
        any_line[0] = my_list[i]
        file_2.write(' '.join(any_line) + '\n')
        i += 1
