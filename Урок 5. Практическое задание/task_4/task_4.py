"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

"""Из задания не совсем понятно нужно выполнить подсчет средней величины дохода всех сотрудников
или только тех у кого зарплата менее 20000.
В моей программе производится подсчет средней величины дохода ВСЕХ сотрудников
"""
from numpy import mean

txt_file = open('salary.txt', 'r', encoding='utf-8')
print('Зарплата меньше 20000 у следующих сотрудников: ')
salary = []
employe = []
for i in txt_file:
    employe = i.split(' ')[0]
    salary = float(i.split(' ')[1])
    if salary < 20000:
        print(employe)
print(f'Средний доход всех сотрудников составляет: {mean(salary)}')
txt_file.close()
