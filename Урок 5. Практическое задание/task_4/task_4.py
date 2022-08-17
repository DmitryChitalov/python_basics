"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


def statistics():
    """Функция сравнения и подсчета среднего дохода"""
    summ = 0
    lst = list()
    try:
        with open('file_task_4.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                lst.extend(line.rstrip().split(' '))
        print("Оклад меньше 20000 у сотрудников: ")
        for i in range(1, len(lst), 2):
            a = int(lst[i])
            summ += a
            count = len(lst) / 2
            if a <= 20000:
                print(lst[i - 1])
        profit = summ / count
        print(f"\nСредняя величина дохода сотрудников: {profit}")
    except FileNotFoundError:
        return 'Файл не найден.'


statistics()
