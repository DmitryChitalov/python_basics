"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

lst = []
average_s = 0
count = 0
with open('salary.txt', 'r') as f:
    for i in f:
        st = i.strip().split()
        average_s += float(st[1])
        count += 1
        if float(st[1]) < 20000:
            lst.append(st[0])
print('Surnames with salary lower then 20 000:')
for _ in lst:
    print(_)
print(f'Average salary is: {average_s / count}')

"""
Ivanov 25000.54
Petrov 13500.23
Sidorov 70000.45
Smirnov 15000.87
Fedorov 8500.79
Usov 34500.99
Konovalov 21000.21
Grigoryev 6000.23
Smolyanov 9000.65
Egorov 1000000.77
"""
