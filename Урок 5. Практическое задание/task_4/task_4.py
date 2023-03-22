"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('staff.txt', 'r', encoding='utf-8') as staff:
    salary_less_20k = []
    total_salary = 0
    staff_unit = 0
    avrg_salary = 0

    for line in staff:
        staff_unit += 1
        name, salary = line.split()

        if float(salary) < 20000.00:
            salary_less_20k.append(name)

        total_salary += float(salary)

    avrg_salary = total_salary / staff_unit

print(f'Оклад менее 20 тысяч у следующих сотрудников: {", ".join(salary_less_20k)}.')
print(f'Средний оклад в компании: {avrg_salary:.2f}')
