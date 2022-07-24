"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open("task_3.txt", "rt", encoding='utf-8') as f_obj:
    cont = f_obj.readlines()
    f_obj.seek(0)
    balance = []
    for i in range(len(cont)):
        line = f_obj.readline()
        words = line.split()
        if float(words[1]) < 20000:
            print(words[0])
        balance.append(words[1])
    print(f'средний доход сотрудников: {sum(map(float, balance)) / len(balance)}')
