"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

 rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
 new_file = []
 with open('file_4.txt', 'r') as file_obj:
     #content = file_obj.read().split('\n')
     for i in file_obj:
         i = i.split(' ', 1)
         new_file.append(rus[i[0]] + '  ' + i[1])
     print(new_file)

 with open('file_4_new.txt', 'w') as file_obj_2:
     file_obj_2.writelines(new_file)
