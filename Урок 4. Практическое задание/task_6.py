"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
+ form itertools import count, cycle
+
+ # a
+ def num_gen(start, end):
+   """ Number Generator """
+   lst = []
+ for number in count(start):
+       if number < end:
+           lst.append(number)
+   else:
+       break
+   return lst
+# б
+ def el_rpt(lst, total):
+   """ Element Repeater """
+   number = 0 
+   new_lst = []
+   for element in cycle(lst):
+       if number < total:
+           new_lst.append(element)
+       else:
+           break
+       number += 1
+   return new_lst
+
+
+ print(num_gen(3, 10))
+ print(el_rpt("ABC", 10))
+
