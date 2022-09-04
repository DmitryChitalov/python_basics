my_dict = {}
with open("task6_notprog.txt", "r", encoding='utf-8') as f_obj:
    content = f_obj.read().split('\n')
    sum_hours = 0
    for line in content:
        line = line.split(' ')
        subj = line[0]
        for el in line:
            if el.isnumeric():
                el = int(el)
                sum_hours = sum_hours + el
        my_dict[subj] = sum_hours
    print(my_dict)

# не могу понять, как сделать сумму отдельной строки, получается только сковзная :(
