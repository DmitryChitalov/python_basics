"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
result = 0
count = 0
list_1 = list()
with open('task_4.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file.readlines():
        list_1.extend(line.rstrip().split(' '))
print("Оклад меньше 20 тыс. у сотрудников: ")
for i in range(1, len(list_1), 2):
    salary = float(list_1[i])
    result += salary
    count = len(list_1) / 2
    if salary <= 20000:
        print(list_1[i - 1])
revenue = result / count
print(f"Средняя величина дохода сотрудников: {revenue}")
