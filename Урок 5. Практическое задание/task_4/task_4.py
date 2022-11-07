"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

LOW_SALARY = 20000.0

low_salary_emp = []
mid_salary = 0

try:
    with open("salaries.dat", encoding="utf-8") as f_obj:
        print("Сотрудники:")
        sum_salary = 0
        emp_cnt = 0
        for line in f_obj:
            print(line, end='')

            items = line.split(' ')
            salary = float(items[1].rstrip())
            sum_salary += salary
            emp_cnt += 1
            if salary < LOW_SALARY:
                last_name = items[0]
                low_salary_emp.append(last_name)

        print()
        mid_salary = sum_salary / emp_cnt
except IOError:
    print("Ошибка!")

print(f"Сотрудники с окладом меньше {LOW_SALARY}")
for emp_name in low_salary_emp:
    print(emp_name)

print(f"Средний доход сотрудников: {avg_salary}")
