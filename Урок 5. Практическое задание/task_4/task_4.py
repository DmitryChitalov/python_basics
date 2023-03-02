"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('salary.txt', 'r') as file:
    low_salary_employees = []
    total_salary = 0
    employee_count = 0
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            salary = float(parts[1])
            total_salary += salary
            employee_count += 1
            # Если оклад меньше 20 тыс., добавить фамилию сотрудника в список low_salary_employees
            if salary < 20000:
                low_salary_employees.append(parts[0])

# Вывести фамилии сотрудников с окладами менее 20 тыс.
if len(low_salary_employees) > 0:
    print('Сотрудники с окладами менее 20 тыс.:', ', '.join(low_salary_employees))
else:
    print('Нет сотрудников с окладами менее 20 тыс.')

# Вычислить среднюю величину дохода сотрудников
if employee_count > 0:
    average_salary = total_salary / employee_count
    print('Средний доход сотрудников:', round(average_salary, 2))
else:
    print('Нет данных о доходах сотрудников.')
