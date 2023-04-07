"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open("text.txt", "r", encoding="utf-8") as f_obj:
    print("Сотрудники, имеющие оклад менее 20 тыс.:")
    content_sum = 0
    content_counter = 0
    while True:
        content = f_obj.readline()
        if content == "":
            break
        content_split = content.split(" ")
        if float(content_split[1]) < 20000:
            print(content_split[0])
        content_sum += float(content_split[1])
        content_counter += 1
    print(f"Средний заработок всех сотрудников: {content_sum / content_counter}")

