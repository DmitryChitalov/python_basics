"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
with open("data_file4.txt", "r+") as df:
    str_spaces = list()
    for s in df.readlines():
        str_spaces.extend(s.rstrip().split(" "))

print("Сотрудники имеющие оклад менее 20 тыс. рублей: ")
summ = 0
for i in range(1, len(str_spaces), 2):
    a = int(str_spaces[i])
    summ += a
    calc = len(str_spaces) / 2
    if a <= 20000:
        print(str_spaces[i - 1])
aver_inc = summ / calc
print(f"\nСредняя величина дохода сотрудников: {aver_inc}")