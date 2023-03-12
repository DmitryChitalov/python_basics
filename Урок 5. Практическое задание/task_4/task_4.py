"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

sum = 0
count = 0
with open("input.txt", "r", encoding="utf-8") as in_file:
    for line in in_file:
        values = line.replace('\n', '').split()
        if len(values) < 2:
            print(f"{line} wrong format")
            continue
        name = values[0]
        salary = float(values[1])
        if (salary < 20_000):
            print(f"{name} has low salary")
        sum += salary
        count += 1

if (count > 0):
    print("Average salary:", sum / count)
else:
    print("File is empty or in wrong format")
