"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open("employees_salary.txt", "r", encoding="UTF-8") as f_obj:
    emp_salary = []
    min_salary = []
    f_list = f_obj.read().split('\n')
    for el in f_list:
        el = el.split()
        if float(el[1]) < 20000.00:
            min_salary.append(el[0])
        emp_salary.append(el[1])
print(f"Оклад менее 20.000,00 у сотрудников: \n"
      f"{min_salary}; \nРазмер среднего оклада составляет: {sum(map(float, emp_salary)) / len(emp_salary)}")
