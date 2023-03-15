"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
salaries = {'A': 17000, 'B': 21000, 'C': 19000, 'D': 15000}
try:
    file_obj = open("test_3.txt", 'w')
    for k,v in salaries.items():
        file_obj.write(k + ': ' + str(v) + "\n")
except IOError:
    print("Ошибка")
finally:
    file_obj.close()
summ = 0
count = 0
workers = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            workers.append(tokens[0])
        summ += int(tokens[1])
        count += 1
avg = summ / count
print(f"Работник(и) с зарплатой менее 20 тыс руб.: {workers}")
print(f"Среднее значение зарплаты: {avg}")