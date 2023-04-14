"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

salary_list = {}
my_list = []

with open("list.txt", encoding='utf=8') as f_obj:
    for line in f_obj:
        my_list.append(line.split())
        salary_list = {el[0]: float(el[1]) for el in my_list}

for key, val in salary_list.items():
    if val < 20000:
        print(f"{key} имеет оклад менее 20 тыс.")

av_solary = sum(salary_list.values()) / len(salary_list)
print(f"Средняя величина дохода сотрудников: {av_solary:.2f}")
