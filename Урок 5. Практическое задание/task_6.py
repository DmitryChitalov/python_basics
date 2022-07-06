"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re
dic = {}
with open("file6.txt", encoding='utf-8') as file:
   for item in file:
         """Создаю словарь, но нужно вычистить значения!"""
         key = item.split(" ")[0].replace(":", "") #Убираю лишние :
         val = item.split(" ")[1:]
         my_str = ' '
         clean = my_str.join(val)
         """ Вытаскиваю числа """
         nums = re.findall(r'\d*\.\d+|\d+', clean)
         nums = [int(i) for i in nums]
         su = sum(nums)  #Суммирую отдельные числа
         dic[key] = su
print(dic)

