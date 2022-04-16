"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
my_temp10 = []
my_temp20 = []
my_sum = []
try:
    with open('test.txt', 'r', encoding='utf-8') as my_file:
        for line in my_file:
            line = line.split()
            my_temp = float(line[1])
            my_sum.append(float(line[1]))
            if float(my_temp) > 10000.00:
                my_temp10.append(line[0] + ' ' + line[1] + '\n')
            if float(my_temp) > 20000.00:
                my_temp20.append(line[0] + ', ')
            print(my_temp)
        print(f'Оклад не мение 10000: ', *my_temp10)
        print(f'Оклад мение 20000 : ', *my_temp20)
        print(f'Средний оклад по {len(my_sum)} сотрудникам : ', round(sum(my_sum) / len(my_sum), 2))
except FileNotFoundError:
    print(f'Error')
