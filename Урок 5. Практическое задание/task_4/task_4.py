"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

def avg(income):
    return round(sum(income)/len(income), 2)

read_file = open("staff.txt", "r", encoding='utf-8')
salaries = []

print("Сотрудники с доходом менее 20000:")
for read_line in read_file.readlines():
    if read_line != "\n":
        array_words = read_line.split(" ")
        salaries.append(float(array_words[1]))
        if float(array_words[1]) < 20000:
            print(array_words[0])
print(f"Средний доход всех сотрудников: ", avg(salaries))
read_file.close()
