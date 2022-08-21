"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
my_file = open("c:\Python38\\text5.txt", "r", encoding="utf-8")

rows = 0
result_salary = 0
while True:
    line = my_file.readline()
    if not line:
        break
    list_line = line.split()
    try:
        fio = list_line[0]
        salary = float(list_line[1])
        if salary < 20000:
            print(f"Сотрудник {fio} оклад {salary}")
    except ValueError:
        salary = 0
    result_salary += salary
    rows += 1
if rows > 0:
    print(f"Средняя зарплата {round(result_salary / rows, 2)}")
my_file.close()
