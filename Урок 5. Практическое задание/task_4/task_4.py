"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open("m_file_1.txt", "r", encoding='utf-8') as m_file:
    peoples = []
    lines = m_file.readlines()
    total = 0
    for line in lines:
        name, salary = line.split()
        salary_num = float(salary)
        total = total + salary_num
        if salary_num < 20000:
            peoples.append(name)
print(f'Оклад меньше 20.000: {", ".join(peoples)}. Средний оклад: {round(total / len(lines))}')
