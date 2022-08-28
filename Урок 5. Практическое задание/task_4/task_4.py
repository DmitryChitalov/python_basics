"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

"""
Выполенине! Емельяненко А.А.
"""


def workers_statistics():
    workers = [['Иванов ', '15000 \n'], ['Сидоров ', '18000 \n'], ['Емельяненко ', '140000 \n'], ['Смирнов ', '90000']]
    try:
        with open('new_file.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])
            r = file.readlines()
            poor = []
            sum = 0
            for i in range(len(r)):
                salary = int((r[i].split())[1])
                if salary < 20000:
                    poor.append((r[i].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников равна {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'


workers_statistics()
