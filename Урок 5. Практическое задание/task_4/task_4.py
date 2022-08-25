"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open("test.txt", 'r', encoding="utf-8") as my_file:
    lines = my_file.read().splitlines()
    dic = {}
    money = []
    for line in lines:
        key, value = line.split(' ')
        dic.update({key: float(value)})
        money.append(float(value))
    for keys, values in dic.items():
        if float(values) < 20000:
            print(f"Сотрудник получающий менее 20000: {keys}")
    print(f"Средняя ЗП: {sum(money) / len(money)} в год")
