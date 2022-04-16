"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

from functools import reduce


min_earning = 20000
earnings = []

with open("task4.txt", "r", encoding = "utf-8") as file:
    line = file.readline()
    while line != "":
        person_info = line.split(" ")
        earning = float(person_info[1])
        if earning < min_earning:
            print(f"{person_info[0]} get earning less than {min_earning}")
        
        earnings.append(earning)
        line = file.readline()


average = reduce(lambda a, b: a + b, earnings) / len(earnings)
print(f"Average earnings = {average}")