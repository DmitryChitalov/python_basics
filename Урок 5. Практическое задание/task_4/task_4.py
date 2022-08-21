"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
my_f = open("task4.txt", encoding='utf-8')
# content = my_f.readlines()
list_empl = []

salary = 0
for i in my_f.readlines():
    content = i.split()
    if int(content[1]) < 20000:
        list_empl.append(i)
    salary = salary + int(content[1])
my_f.close()
print("Сотрудники с окладом мение 20000:")
for i in list_empl:
    print(i)
print(f"Средняя величина оклада всех сотрудников: {salary / 4}")
