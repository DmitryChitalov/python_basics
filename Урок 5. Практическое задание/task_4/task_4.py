"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('file_4.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
average_salary = 0.0
for line in lines:
    data = line.split(' ')
    salary = float(data[1])
    average_salary += salary
    if salary < 20000:
        print(f"Worker with surname {data[0]} has salary less than 20K")
average_salary /= len(lines)
print(f"Average salary: {average_salary}")
