"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


with open('sal_file', 'r', encoding='utf_8') as my_file:
    salary = []
    clerks = []
    my_list = my_file.read().split('\n')
    for line in my_list:
        res = line.split()
        if int(float(res[1])) < 20000:
            clerks.append(res[0])
        salary.append(res[1])
print(f'Оклад меньше 20.000 у сотрудников: {clerks}\nСредний оклад {sum(map(float, salary)) / len(salary)}')

