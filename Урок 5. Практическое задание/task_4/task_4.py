"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('text4.txt', 'r') as collective:
    salary = []
    fix = []
    listing = collective.read().split('\n')
    for k in listing:
        k = k.split()
        if float(k[1]) < 20000:
           fix.append(k[0])
        salary.append(k[1])
print(f'Оклад менее 20.000- {fix}, средняя з/п: {sum(map(float, salary)) / 10:.2f}')