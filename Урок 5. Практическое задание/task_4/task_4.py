"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


def generator_list_1():
    list_1 = open('list_1.txt', 'w')
    data_list_1 = [
        'Иванов 23500.50',
        'Петров 13600.70',
        'Сидоров 15500.20',
        'Страроверов 25000.90',
        'Имбрамнурласов 19900.60',
        'Салахов 19200.15',
        'Авчинников 38000.40',
        'Гусев 90000.00',
        'Сарокин 12500.45',
        'Гафонов 37800.25',
        'Романова 165124.32',
    ]
    data = [
        list_1.write(str(data_list_1[i]) + "\n") for i in
        range(len(data_list_1))
    ]
    list_1.close()


generator_list_1()


def check_salary():
    list_1 = open('3.txt', 'r')
    data = list_1.read()
    data_list = data.strip().split('\n')
    data_dict = {
        data_list[list_i].split()[el]: data_list[list_i].split()[el + 1]
        for list_i in range(len(data_list))
        for el in range(len(str(list_i).split()))
    }
    list_person = []
    for key, value in data_dict.items():
        if float(value) < 20000.00:
            list_person.append(key)

    return "Список сотрудников с окладом менее 20 000: " + str(list_person)
