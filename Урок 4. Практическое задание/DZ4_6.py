from itertools import cycle, count
#Итератор от начального значения до конечного
begin_count = int(input("Введите начальное значение "))
end_count = int(input("Введите конечное значение "))
for el in count(begin_count):
    if el > end_count:
        break
    else:
        print(el)

#Итератор повторения элементов списка

my_list = ['A', 'b', 'C']
i = 0
for el in cycle(my_list):
    if i > end_count:
        break
    else:
        print(el)
        i += 1
