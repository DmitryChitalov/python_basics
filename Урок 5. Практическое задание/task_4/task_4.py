"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
lines_count = 0
awards_sum = 0
names_list = []
with open("input_file.txt", "r", encoding='utf-8') as f_obj:
    while True:
        line = list(f_obj.readline().split())
        if not line:
            break
        if float(line[1]) < 20000:
            names_list.append(line[0])
        awards_sum += float(line[1])
        lines_count += 1
print("Фамилии сотрудников с окладом менее 20000: ", end="")
print(", ".join(el for el in names_list))
print(f"Средняя зарплата сотрудников: {awards_sum / lines_count}")
