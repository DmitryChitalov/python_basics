"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
data_from_file = []
employers_total_selery = 0
enployers_with_small_selery = []

try:
    with open("selery.txt") as f_obj:
        for line in f_obj:
            data_from_file.append(line.split())
except IOError:
    print("проблема с открытием файла. возможно его нет")

for el in data_from_file:
    employers_total_selery += float(el[1])
    if float(el[1]) < 20000:
        enployers_with_small_selery.append(el[0])

print(f"менее 20 тыс: {', '.join(enployers_with_small_selery)}")
print(f"средней величины дохода сотрудников {(employers_total_selery / len(data_from_file)):.2f}")
