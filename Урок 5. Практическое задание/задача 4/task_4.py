"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
persons = {}
fr = open("persons.txt", "r")
for line in fr:
    person, salary = line.split()
    persons[person] = float(salary)
fr.close()

low_salary = {person: salary for (person, salary) in persons.items() if salary < 10000}
mid = sum(persons.values()) / len(persons)

print(f"Low salary: {low_salary}")
print(f"Mid salary: {mid}")
