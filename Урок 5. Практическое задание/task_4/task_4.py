"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
line_cnt = 0
total_salary = 0
temp_list = []
file_obj = open("salary.txt", encoding="utf8")
for line in file_obj:
    line_cnt += 1
    temp_list = line.split()
    total_salary = total_salary + float(temp_list[1])
    if float(temp_list[1]) < 20000:
        print(f"У {temp_list[0]} оклад менее 20000. Оклад работника: {temp_list[1]}")
file_obj.close()
print(f"Средний оклад по организации: {total_salary / line_cnt:.2f}")
