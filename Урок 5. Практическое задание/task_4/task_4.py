"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('Data.txt', 'r', encoding='utf-8') as my_file:
    pay = []
    less = []
    new_list = my_file.read().split('\n')
    for i in new_list:
        i = i.split()
        if int(i[1]) < 20000:
            less.append(i[0])
        pay.append(i[1])
print(f'Меньше 20 тысяч получают {less}, средний доход сотрудников составляет {sum(map(int, pay)) / len(pay)}')

