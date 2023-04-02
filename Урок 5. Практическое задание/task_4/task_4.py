"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
#!/usr/bin/env python3
import os

print("Внимание, текущая папка:", os.getcwd())

data_store = {}
salary_cap = 20000

with open("input_file4.txt", 'r') as source_file:
    source_data = source_file.readlines()

    for i in source_data:
        splitting_lines = i.split()
        data_dict_key = splitting_lines[0].split()
        data_dict_value = list(map(float, splitting_lines[1].split()))
        data_store.update({data_dict_key[0]: data_dict_value[0]})

below_the_line = [key for key, value in data_store.items() if value < salary_cap]
print(f"Список сотрудников с окладом менее {salary_cap:.2f}: ", ", ".join(below_the_line))
print(f"Средняя величина дохода сотрудников: {sum(data_store.values()) / len(data_store):.2f}")
