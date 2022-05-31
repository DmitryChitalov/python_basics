"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('staff.txt', encoding='utf-8') as f_staff:
    salary = []
    last_names = []
    my_list = f_staff.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            last_names.append(i[0])
            salary.append(i[1])
            average_salary = sum(map(float, salary)) / len(salary)
    print(f'Оклад менее 20000 рублей имеют: {last_names} \n'
          f'Средняя величина дохода этих сотрудников: {round(average_salary, 2)}')
