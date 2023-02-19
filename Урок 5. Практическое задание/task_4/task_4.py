"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
first_f = open("empsal.txt", "r", encoding='utf-8')
lines = first_f.readlines()
first_f.close()
total = 0
count = 0
for line in lines:
    surname, salary = line.split()
    count += 1
    total += int(salary)
    if int(salary) < 20000:
        print(f"Surname: {surname} salary: {salary}")
print (f"Average salary: {total/count}")
