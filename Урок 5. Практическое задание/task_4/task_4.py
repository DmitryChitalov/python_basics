"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
work_dict = {}

with open("employes.txt", "r") as file:
    work_list = file.read().split()
    val_list = [work_list[i] for i in range(1, len(work_list), 2)]
    key_list = [work_list[i] for i in range(0, len(work_list), 2)]
    work_dict = dict(zip(key_list, val_list))

print('Сотрудники с окладом менее 20 тыс.:')
for key in work_dict:
    if float(work_dict.get(key)) < 20000.00:
        print(f'{key} {work_dict.get(key)}')

total_salary = 0

for key in work_dict:
    total_salary += float(work_dict.get(key))
    
av_salary = round(total_salary / len(key_list), 2)
print(f'Средний оклад в коллективе:\n {av_salary}')
