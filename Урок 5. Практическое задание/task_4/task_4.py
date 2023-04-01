"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

from statistics import mean

if __name__ == '__main__':
    try:
        with open('pay.txt', 'r', encoding='utf-8') as string_obj:
            family = ''
            min_pay = []
            mid_pay = []
            for i in string_obj:
                for el in i.split():
                    if not el.replace('.', '').isdigit():
                        family = el
                    else:
                        min_pay.append(family) if float(el) < 20000 else ''
                        mid_pay.append(float(el))
            print(f"Список сотрудников с окладом менее 20000 рублей: {', '.join(min_pay)}")
            print(f"Средняя величина дохода сотрудников: {mean(mid_pay)} рублей.")
    except Exception as e:
        print(e)
