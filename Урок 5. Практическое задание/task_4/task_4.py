"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

my_dict = {}
average_salary = 0.0

my_f = open("input_ex4.txt", "r", encoding='utf-8')
for string in my_f:
    my_list = list(string.split())
    x = float(my_list[1])
    my_dict[my_list[0]] = x    
for key in my_dict.keys():
    if my_dict[key] < 20000:
        print(f"Сотрудник {key} зарабатывает меньше 20 000")   
    average_salary = average_salary + my_dict[key]               
print(f"Средняя величина дохода сотрудника {average_salary/len(my_dict)}")
my_f.close()
