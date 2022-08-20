"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
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
