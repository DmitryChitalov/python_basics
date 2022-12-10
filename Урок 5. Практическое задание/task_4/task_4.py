"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

from statistics import mean


file_in = 'my_file.txt'

names_people = []
with open(file_in, 'r', encoding='UTF-8') as fl:

    for i in fl.readlines():
        names_people.append(i.replace('\n', '').split())

min_lst = {}
avg_lst = {}
for name in names_people:
    avg_lst[name[0]] = float(name[1])
    if float(name[1]) < 20000:
        print(f"У сотрудника с фамилией {name[0]} разаботок ниже 20 т.р.")
        min_lst[name[0]] = float(name[1])


print(
    f"Средняя сумма заработка лиц с доходом менее 20 т.р. составляет:\
 {round(mean(min_lst.values()), 2)}"
)

print(
    f"Средний доход всех участников списка составляет: {round(mean(avg_lst.values()), 2)}")

# Альтернативный метод, без "mean"
print(
    f"Средний доход всех участников списка составляет:\
 {round(sum(avg_lst.values()) / len(avg_lst), 2)}"
)
