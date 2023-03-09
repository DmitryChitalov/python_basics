"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""


def workers_statistics():
    workers = [['Иванов ', '11000 \n'], ['Сидорв ', '17000 \n'], ['Петров ', '141000 \n'], ['Смирнов ', '90000']]
    try:
        with open('new_file.txt', 'r+', encoding="utf-8") as file:
            for i in range(len(workers)):
                file.writelines(workers[i])
            l = file.readlines()
            poor = []
            sum = 0
            for i in range(len(l)):
                salary = int((l[i].split())[1])
                if salary < 20000:
                    poor.append((l[i].split())[0])
                sum += salary
            print(f'Средняя величина дохода сотрудников равна {sum / len(workers) / 12:.2f}')
            print(f'Меньше 20 тыс. рублей получает сотрудник: {", ".join(poor)}')
    except FileNotFoundError:
        return 'Файл не найден.'
workers_statistics()
