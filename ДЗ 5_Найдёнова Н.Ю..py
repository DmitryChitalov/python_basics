#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Задание 1. Создать программно файл в текстовом формате,записать в него построчно данные, вводимые пользователем.Об окончании 
#ввода данных.свидетельствует пустая строка.

f_obj = open("output_file.txt", 'w', encoding='utf-8')
lines = []
while True:
    line = input("Введите новые данные или введите Enter для завершения: ")
    if line != '':
        lines.append(line + "\n")
    else:
        break
f_obj.writelines(lines)

with open("output_file.txt", "r", encoding='utf-8') as f_obj:
    content = f_obj.readlines()
    print(content)

with open("output_file.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line)


# In[2]:


#Задание 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,выполнить подсчет количества строк, количества слов 
#в каждой строке.

count_lines = 0
count_words = 1

with open("joke.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line.replace('\n', ''))
        for n in line:
            if n == " ":
                count_words += 1
        count_lines += 1
        print(f"Количество слов в строке {count_lines} = {count_words} \n")
        count_words = 1
    print(f"В файле {count_lines} строк(и)")


# In[3]:


#задание 3. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.При этом английские числительные 
#должны заменяться на русские.Новый блок строк должен записываться в новый текстовый файл.

dict_int = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("input_file.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in dict_int.keys():
            line = line.replace(key, dict_int[key])
        print(line)
        with open("output_file.txt", "a") as f_rus:
            f_rus.write(f"\n {line}")


# In[1]:


#Задание 4. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
#и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
#Пример файла:
#Иванов 23543.12
#Петров 13749.32

firm = {'Силин': 23128, 'Жилин': 27340, 'Васильев': 15000, 'Козырев': 11500,'Булычев': 18900,'Симонов': 45000,"Валдырев": 27500, 
        "Любавина": 24320, 'Сироткина': 22150, "Пузырева": 35700}
try:
    file_obj = open("test3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"averate: {result}")


# In[2]:


#Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна 
#подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('file2.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')
summary()


# In[12]:


#Задание 6.Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
#практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были 
#все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на 
#экран.
#Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#Физика:   30(л)   —   10(лаб)
#Физкультура:   —   30(пр)   —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def sum_in_line(line):
    res = 0
    for el in line.split():
        try:
            res += int(el)
        except ValueError:
            pass
    return res

key_list = []
with open("subjects.txt", "r", encoding='utf-8') as file:
    work_list = file.read().split()
    key_list = [work_list[i] for i in range(0, len(work_list) - 1, 7)]

lessons = []
with open("subjects.txt", "r", encoding='utf-8') as file:
    for line in file:
        lessons.append((sum_in_line(line)))

subj_dict = dict(zip(key_list, lessons))
print(subj_dict)


# In[10]:


#задание 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о 
#фирме:название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1   ООО   10000   5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, 
#в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а 
#также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.

def rent_in_line(line):
    for i in range(2, 3):
        rent = int(line[i]) - int(line[i + 1])
    return rent

good_firms = []
rent_list = []

with open('Firms.txt', 'r', encoding='utf-8') as file:
    for line in file:
        rent = (rent_in_line(line.split()))
        if rent > 0:
            good_firms.append(line.split())
            rent_list.append(rent)
total = 0
for el in rent_list:
    total += el
av_rent = total / len(rent_list)
profit_dict = {'average_profit': av_rent}

firmas_list = []
for el in good_firms:
    firmas_list.append(el[0])

profit_firms = dict(zip(firmas_list, rent_list))
profit_list = [profit_firms, profit_dict]

import json

with open('profit_companines.json', 'w') as out_file:
    json.dump(profit_list, out_file)


# In[ ]:





# In[ ]:




