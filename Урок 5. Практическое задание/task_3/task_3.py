"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

employees = {}
with open("salary_file.txt", "r", encoding='utf-8') as file:
    for line in file:
        (key, val) = line.split()
        employees[key] = val
print(employees)

sum_salary = 0
for key in employees:
    sum_salary = sum_salary + float(employees[key])
    if float(employees[key]) >= 20000:
        print(key)
print(f"Средняя величина дохода сотрудников составляет: {round(sum_salary / len(employees))}")
