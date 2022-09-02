my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus = []
with open("task3_notprog.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        line = line.split(' ', 1)
        rus.append(my_dict[line[0]] + ' ' + line[1])
    print(rus)

with open("task3_prog.txt", "w", encoding='utf-8') as f_obj:
    f_obj.writelines(rus)
