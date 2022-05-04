def generator_file3():
    f_file_open = open('3.txt', 'w')
    data_list = [
                'Иванов 23500.50',
                'Петров 13600.70',
                'Сидоров 15500.20',
                'Морозов 25000.90',
                'Новиков 19900.60',
                'Волков 19200.15',
                'Голубев 38000.40',
                'Беляев 90000.00',
                'Андреев 12500.45',
                'Филатов 37800.25',
                ]
    data = [
        f_file_open.write(str(data_list[i]) + "\n") for i in range(len(data_list))
    ]
    f_file_open.close()
generator_file3()
def check_salary():
    f_file_open = open('3.txt', 'r')
    data = f_file_open.read()
    data_list = data.strip().split('\n')
    data_dict = {
        data_list[list_i].split()[el] : data_list[list_i].split()[el+1]
        for list_i in range(len(data_list))
        for el in range(len(str(list_i).split()))
    }
    list_person = []
    for key, value in data_dict.items():
        if float(value) < 20000.00:
            list_person.append(key)

    return "Список сотрудников с окладом менее 20 000: " + str(list_person)
print(check_salary())