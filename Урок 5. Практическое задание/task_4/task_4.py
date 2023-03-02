"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('less5_t4_salary.txt', 'r', encoding='utf-8') as txt:
    salaries = {line.split()[0].strip(): int(line.split()[1]) for line in txt.readlines()}
sum_of_salaries = 0
for surname, salary in salaries.items():
    sum_of_salaries += salary
    if salary < 20000:
        print(f"Сотрудник {surname} получает оклад менее 20 тыс.Р")
average_salary = sum_of_salaries / len(salaries)
print(f'Средняя величина дохода сотрудников = {average_salary}')