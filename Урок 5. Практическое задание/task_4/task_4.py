"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


def get_salary(some_str):
    str_num = ""
    for el in some_str:
        if el.isnumeric() or el == ".":
            str_num = str_num + el
    return float(str_num)


def get_surname(some_str):
    surname = ""
    for el in some_str:
        if el != " ":
            surname = surname + el
        else:
            break
    print(surname)
    return surname


input_file = open('inputtextfile.txt', 'r')
list_of_not_so_happy_people = []
for line in input_file:
    if get_salary(line) < 20000:
        list_of_not_so_happy_people.append(get_surname(line))

print(list_of_not_so_happy_people)
input_file.close()
