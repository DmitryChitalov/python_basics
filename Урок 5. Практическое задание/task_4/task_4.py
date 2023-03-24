"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

#Lines = ["emp1 9416.52\n", "emp2 24722.12\n", "emp3 12844.89\n", "emp4 21226.13\n", "emp5 22503.27\n", "emp6 12036.85\n", "emp7 9797.44\n", "emp8 10930.56\n", "emp9 13900.51\n", "emp10 30344.98\n", "emp11 11532.98\n", "emp12 20352.82\n", "emp13 33586.52\n", "emp14 8197.24\n", "emp15 30698.65\n"]
 
file1 = open('salaries.txt', 'r')
Lines = file1.readlines()
 
sum = 0.0
for line in Lines:
    salary = float(line.split()[1])
    sum += salary
    if(salary<10000):
        print("{} has salary less than 10K, his salary {}".format(line.split()[0], salary))

print("Average Salaries is {}".format(sum/len(Lines)))
