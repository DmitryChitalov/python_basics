"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open("out_file.txt", "w", encoding='utf-8') as f_obj :
    temp_line = input('Введите текст')
    while len(temp_line) > 0 :
        f_obj.writelines(temp_line + "\n")
        temp_line = input('Введите текст')

"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("file_for_task_2.txt", "r", encoding='utf-8') as f_obj :
    i = 0
    for line in f_obj:
        i += 1
        temp_line = line.split()
        print(f"Количество слов в строке =  {len(temp_line)}")
    print(f"Количество строк в файле =  {i}")


"""
3)
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
with open("file_for_task_3.txt", "r", encoding='utf-8') as f_obj :
    temp_list = []
    for line in f_obj:
        if line.startswith('One'):
            temp_list.append(line.replace('One','Один'))
        elif line.startswith('Two'):
            temp_list.append(line.replace('Two','Два'))
        elif line.startswith('Three'):
            temp_list.append(line.replace('Three','Три'))
        elif line.startswith('Four'):
            temp_list.append(line.replace('Four','Четыре'))

with open("file_for_task_3_2.txt", "w", encoding='utf-8') as rez_obj :
    rez_obj.writelines(temp_list)

"""
4)
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open("file_for_task_4.txt", "r", encoding='utf-8') as f_obj:
    name_list = []
    pay_list = []
    for line in f_obj:
        temp_list = line.split()
        for i in range (0, len(temp_line)):
            name_list.append(temp_list[0])
            pay_list.append(temp_list[1])

rezult = 0
for i in range (0, len(pay_list)):
    rezult = float(pay_list[i]) + rezult
    if float(pay_list[i]) < 20000:
        print(f'{name_list[i]} имеет оклад менее 20 тыс')
print(f'Cредняя зарплата сотрудника =  {rezult/len(pay_list)}')

"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open("file_for_task_5.txt", "w", encoding='utf-8') as f_obj :
    some_line = input('Введите числа через пробел')
    # rezult = 0 - если нам нужно суммировать все числа из файла, то объявляем rezult только здесь, ниже убираем
    while len(some_line) > 0:
        rezult = 0
        some_list = some_line.split()
        for i in range(0, len(some_list)):
            rezult = int(some_list[i]) + rezult
        f_obj.writelines(some_line +"\n")
        some_line = input(f'Сумма чисел равняется {rezult}.Для продолжения введите новые числа через пробел, а для выхода - пустую строку')


"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и 
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open("file_for_task_6.txt", "r", encoding='utf-8') as f_obj :
    rezult_dict = {}
    for line in f_obj:
        temp_line = line.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace(".", "")
        subject, lecture, practice, lab = temp_line.split()
        lect_int = 0
        practice_int = 0
        lab_int = 0
        if lecture != "-":
            lect_int = int(lecture)
        if practice != "-":
            practice_int = int(practice)
        if lab != "-":
            lab_int = int(lab)
        rezult_dict[subject] = lect_int + practice_int + lab_int
    print(f"{rezult_dict}")


"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
 содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
with open("file_for_task_7.txt", "r", encoding='utf-8') as f_obj :
    pro_list = []
    firm_dict = {}
    i = 0
    for line in f_obj:
        i =+ 1
        profit = 0
        name, forms, vy, ub  = line.split()
        profit = int(vy) - int(ub)
        pro_list.append(profit)
        firm_dict [name] = profit
    sum_profit = 0
    k = 0
    for i in pro_list:
        if i > 0:
            sum_profit = sum_profit + i
            k += 1
    avg_profit = sum_profit/k
    avg_dict = {"average_profit" : avg_profit}
    j_list = [firm_dict, avg_dict]
    print(j_list)
with open("file_for_task_7.json", "w", encoding='cp1251') as j_obj:
    json.dump(j_list, j_obj)
print(f"{firm_dict} {avg_dict}")

