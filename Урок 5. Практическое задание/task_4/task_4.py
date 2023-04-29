"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
dict_file = {}
with open('file.txt', 'r', encoding='utf-8') as file:
    while True:
        try:
            files = file.readline().split(' ')
            files[1] = files[1].replace('\n', '')
            dict_file[files[0]] = files[1]
        except IndexError:
            break

min_salary = []
all_salary = []
for key, value in dict_file.items():
    all_salary.append(float(value))
    if float(value) < 20000:
        min_salary.append(key)

print(f'\nОклад сотрудников менее 20 тыс. - {", ".join(min_salary)}')
print(f'Среднняя величина оплаты сотрудинков - {sum(all_salary)/len(all_salary):0.2f}')
