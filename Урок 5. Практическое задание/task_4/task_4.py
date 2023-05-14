"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить,
кто из сотрудников имеет оклад менее 20 тыс.,вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('text_file_4.txt', 'r', encoding='utf-8') as my_f:
    print(f"Оклад сотрудников меньше 20 тыс.: ")
    sum_salary = 0
    n = 0
    for line in my_f:
        my_string = line.split(' ')
        y = my_string[1].rstrip()
        x = float(y)
        if x < 20000:
            print(f"{my_string[0]}")
            n += 1
            sum_salary = sum_salary + x
    average_income = round(sum_salary / n, 2)
    print(f"Средняя величина дохода этих сотрудников: {average_income}")
