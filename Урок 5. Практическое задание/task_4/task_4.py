"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('salary.txt', "r", encoding='UTF-8') as file:
    all_salary = 0
    quantity_employees = 0
    for elem in file:
        surname, salary = elem.split()
        salary = float(salary)
        if salary < 20000:
            print(f'{surname}: {salary}')
        all_salary += salary
        quantity_employees += 1
    average_salary = all_salary / quantity_employees
    print("Средний доход работников:", average_salary)
