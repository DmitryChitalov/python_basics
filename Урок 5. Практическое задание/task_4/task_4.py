"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

employee_list = []
total_money = 0
employee_count = 0

with open("salaries.txt") as f:
    string_list = f.readlines()
    for line in string_list:
        employee_count += 1
        employee = line.split()
        total_money += float(employee[1])
        if 20000 < float(employee[1]):
            employee_list.append(employee[0])

print(f"Employes with salary over 20000 is: {employee_list}")
print(f"Average salary is: {total_money/employee_count}")
