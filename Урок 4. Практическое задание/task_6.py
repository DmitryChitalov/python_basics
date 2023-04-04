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
from itertools import count, cycle


def func_generator(start, stop):
    result = []
    for i in count(start):
        if i <= stop:
            result.append(i)
        else:
            break
    print(f"Список чисел: {result}")

first_number = int(input('Введите начальное число: '))
end_number = int(input('Введите последнее число: '))
func_generator(first_number, end_number)


my_list = ['test ', 'AAA ', 11, ' proverka ']

def func_list(my_list):
    n = 0
    result = ""
    for i in cycle(my_list):
        if n >= end_list:
            break
        result = result + str(i)
        n += 1
    print(f"Результат выполнения: {result}")

end_list = int(input(' Введите сколько значений необходимо вывести из списка: '))
func_list(my_list)