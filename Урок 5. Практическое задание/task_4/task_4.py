"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

try:
    salary_sum = 0
    salary_set = 20000
    row_count = 0

    with open("data.txt", encoding="utf-8") as f:
        for line in f:
            if float(line.split(' ')[1]) < salary_set:
                print(f"{line.split(' ')[0]} имеет оклад менее {salary_set} руб - {line.split(' ')[1]}")
            salary_sum += float(line.split(' ')[1])
            row_count += 1
    print(f"Средний размер дохода сотрудников: {round(salary_sum / row_count, 2)} рублей")

except BaseException as e:
    print(f"General error: {e}")

except IOError as e:
    print(f"IOError: {e}")
