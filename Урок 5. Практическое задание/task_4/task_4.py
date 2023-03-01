"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

fp = open("employees.txt", "r", encoding="utf-8")

employees = []
salaries = []

for line in fp:
    line = line.split()
    salaries.append(float(line[1]))
    if float(line[1]) < 20000:
        employees.append(line[0])

fp.close()

salaries.sort()
print("Сотрудники с доходом ниже 20000₽: " + ", ".join(employees))
print(f"Средняя зарплата среди сотрудников: {sum(salaries) / len(salaries):.2f}")
print(f"Средняя медианная зарплата среди сотрудников: {salaries[len(salaries) // 2]}")
