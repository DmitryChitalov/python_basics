with open("task4_notprog.txt", "r", encoding='utf-8') as f_obj:
    content = f_obj.read()
    my_list = content.split('\n')
    last_name = []
    sal = []
    for line in my_list:
        line = line.split(' ')
        if int(line[1]) < 20000:
            print(f"Зарплата меньше 20 000 у сотрудника по фамилии {line[0]}")
        sal.append(line[1])
        sum_sal = sum(map(int, sal))
        mean_sal = sum_sal / len(sal)
    print(f"Средняя величина дохода сотрудников: {mean_sal}")
