"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

all_salary = []
with open("text.txt", encoding="utf8") as my_file:
    for i in my_file:
        lastname = i.split()[0]
        salary = i.split()[-1]
        salary = float(salary.replace(',', '.'))
        all_salary.append(salary)
        if salary < 20000:
            print(lastname)
print(f"Средняя зарплата: {sum(all_salary)/len(all_salary):.2f}")
