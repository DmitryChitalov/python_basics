"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('les5_task3_text.txt', 'r', encoding='utf-8') as txt:
    salaries = {line.split()[0].strip(): int(line.split()[1]) for line in txt.readlines()}
sum_of_salaries = 0  
for surname, salary in salaries.items():  # перебор словаря
    sum_of_salaries += salary
    if salary < 20000:
        print(surname)
average_salary = sum_of_salaries / len(salaries)
print(f'Средняя величина дохода сотрудников равна {average_salary}')
