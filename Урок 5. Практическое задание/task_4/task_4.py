"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


firm = {'Иванов': 23543.12, 'Петров': 13749.32}
try:
    file_obj = open("info.txt", 'r')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + '\n')
except IOError:
    print("Произошла ошибка ввода-вывода!")

finally:
    file_obj.close()
summary = 0
count = 2
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 150:
            persons.append(tokens[0])
        summary += int(tokens[1])
        count += 1
#result = summary / count
print(f"persons: {persons}")
#print(f"averate: {result}")
