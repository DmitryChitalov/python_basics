"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

m = []
s = 0
try:
    with open('t4.txt', 'r', encoding="utf-8") as t_obj:
        cont = t_obj.read().split("\n")
        for st in cont:
            st = st.split()
            s += float(st[1])
            if float(st[1]) < 20000:
                m.append(st[0] + '\n')
    print("Оклад меньше 20 тыс. руб.:\n", *m)
    print("Средний оклад: ", round(s / int(len(cont)), 2))
except FileNotFoundError:
    print("Файл не найден!")