"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

report = []
so = 0
with open('test.txt', 'r', encoding='UTF-8') as sp:
     rows = sp.readlines()
     print("Оклады сотрудников:")
     for row in rows:
         row_items = row.split(' ')
         report.append([row_items[0], float(row_items[1])])
         print(f"{row_items[0]} - {float(row_items[1])} руб.")
         so += float(row_items[1])
print("\nСотрудники с окладом менее 20000 руб.:")
[print(worker[0]) for worker in report if worker[1] < 20000]
print(f"\nСредний оклад сотрудников {so / len(report)} руб.")
