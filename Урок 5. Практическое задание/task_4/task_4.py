"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

all_sum = 0
count = 0
example_wage = 20000.00
family_count = ''

with open('example.txt', 'r') as file:
    for i in file:
        date = i.rstrip('\n').split()
        wage = float(date[1])
        all_sum += wage
        count += 1

        if wage < example_wage:
            family_count += f'{date[0]} '

mean_summ = all_sum / count
summ_correct = round(mean_summ, 2)

print(f'Зарплату менее {example_wage} получают {family_count}')
print(f'Средняя зарплата составляет: {summ_correct}')
