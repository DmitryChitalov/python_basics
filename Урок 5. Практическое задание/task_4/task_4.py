"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('task4.txt', 'r', encoding='utf-8') as f:
    workers = {}
    average_salary = 0
    counter = 0
    for line in f:
        key, value = line.split()
        workers[key] = value
        counter += 1
        average_salary += int(value)
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
    print(f"Средний оклад сотрудников -  {average_salary / counter}")

