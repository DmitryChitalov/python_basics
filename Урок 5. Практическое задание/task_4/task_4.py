"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open("lesson5-4.txt", "r", encoding="utf-8") as my_file:
    workers = {}
    for line in my_file:
        key, value = line.split()
        workers[key] = int(value)
        if int(value) < 20000:
            print(f"{key}: Оклад менее 20 тыс.")
average_value = sum(workers.values()) / len(workers)
print(f"Средний доход сотрудников = {average_value}")


