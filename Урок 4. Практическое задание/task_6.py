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

#a
class IntGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start += 1
            return value
        else:
            raise StopIteration

for num in IntGenerator(3, 10):
    print(num)

#b
from itertools import cycle

class ListIterator:
    def __init__(self, lst, count):
        self.lst = lst
        self.count = count
        self.iter = cycle(self.lst)
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.count:
            value = next(self.iter)
            self.counter += 1
            return value
        else:
            raise StopIteration

for elem in ListIterator(['a', 'b', 'c'], 3):
    print(elem)

