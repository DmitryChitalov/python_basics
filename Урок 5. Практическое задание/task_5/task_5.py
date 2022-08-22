"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('text.txt', 'w', encoding='utf-8') as f:
    text = input('Числа через пробел: ')
    f.write(text)
with open('text.txt', 'r', encoding='utf-8') as r:
    lst = r.read().split()
    print(f'Сумма чисел = {sum(map(int, lst))}')

