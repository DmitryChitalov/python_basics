"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
from statistics import mean

SALARY = 20000

if __name__ == '__main__':
    try:
        with open('text', 'r') as f_obj:
            name = ''
            min_s = []
            all_s = []
            for i in f_obj:
                for el in i.split():
                    if not el.replace('.', '').isdigit():
                        name = el
                    else:
                        min_s.append(name) if float(el) < SALARY else ''
                        all_s.append(float(el))
            print(f"Сотрудники с окладом менее {SALARY}: {', '.join(min_s)}")
            print(f"Средняя величина дохода сотрудников: {mean(all_s)}")
            del name, min_s, all_s
    except IOError:
        print('Warning: error input output')
    except Exception as e:
        print(e)
