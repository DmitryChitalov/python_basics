"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# Выводим название программы
print('Программа которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов')

# Определяем функцию
def __max_from_3num(incom_list):
    incom_list_sort = incom_list
    incom_list_sort.sort()
    print(f'Сортированыый список при помощи .sort(): {incom_list_sort},\n'
          f'Cумма двух наибольших значений - {incom_list_sort[1]+incom_list_sort[2]}')
    incom_list.remove(min(incom_list))
    sum_max = sum(incom_list)
    print(f'Сумма двух наибольших значений не используя .sort(): {sum_max}')


# Запрашиваем данные и передаем в функцию
temp_list = input('Введите три числа через пробел:\n').split(' ')
temp_list = list(map(int, temp_list))
__max_from_3num(temp_list)
