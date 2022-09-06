"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('employees.txt', 'r', encoding="utf-8") as f_obj:
    total_salary_sum = 0
    line_num = 0
    for line in f_obj:
        person_salary = float(line.split()[1])
        total_salary_sum += person_salary
        if person_salary < 40000:
            print(f"{line.split()[0]} - {person_salary}")
        line_num += 1
print(f"Средняя величина дохода сотрудников: {total_salary_sum/line_num}")