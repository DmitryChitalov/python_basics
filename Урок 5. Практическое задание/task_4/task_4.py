"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open('my_file4.txt', 'r', encoding='utf-8') as my_file:
    my_string = []
    for line in my_file:
        my_string.append(line.split(' '))


loop = []
summ = 0
print(my_string)

for line in my_string:
    summ += float(line[1].rstrip())
    if float(line[1].rstrip()) < 20000:
        loop.append(line[0])


print(f"Меньще 20к получают : {', '.join(loop)}")
print(f'Средняя величина дохода = {summ/len(my_string):.2f}')
