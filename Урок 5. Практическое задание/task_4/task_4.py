"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
open_file = open("task_file4.txt", encoding="utf8")
new_file = open("task_file4_new.txt", "w", encoding="utf8")
my_list = []

for line in open_file:
    my_list = line.split()
    my_list[0] = my_dict.get(my_list[0])
    new_file.write(" ".join(my_list))
    new_file.write("\n")

open_file.close()
new_file.close()