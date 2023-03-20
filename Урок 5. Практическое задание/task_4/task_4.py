"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
f_obj = open("file.txt")
# with open("file.txt") as f_obj:

list_of_list = [line.split()[0] for line in f_obj if float(line.split()[1]) < 20000]
print(list_of_list)

f_obj.seek(0)

# with open("file.txt") as f_obj:
list_of_salary = [float(line.split()[1]) for line in f_obj]

print("Средняя зарплата сотрудников: {:.2f}".format(sum(list_of_salary)/len(list_of_salary)))
