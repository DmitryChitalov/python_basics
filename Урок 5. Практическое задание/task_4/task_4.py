"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

firm = {'Васильев': 151000.00, 'Захаров': 120000.00, 'Крайнов': 141000.00,
        'Мамонтов': 21000.00, 'Насибулин': 12000.00, 'Миронов': 100000.00,
        'Иванов': 85000.00, 'Григорьев': 25000.00, 'Конев': 56000.00,
        'Тарасов': 50000.00, 'Филатов': 250000.00, 'Придурок': 1000.00,
        'Баранов': 45000.00}
try:
    file_obj = open("test_file.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
my_sum = 0
counts = 0
persons = []
with open("test_file.txt", "r") as file_obj:
    for line in file_obj:
        tokens = line.split(':')
        if float(tokens[1]) <= 20000:
            persons.append(tokens[0])
        my_sum += float(tokens[1])
        counts += 1
salary_avrg = my_sum / counts
print(f"Оклад менее 20000: {persons}")
print(f"Средний оклад: {int(salary_avrg)}")