"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

# создание текстового файла с набором чисел, разделенных пробелами
n = int(input("Введите количество записываемых чисел: "))
numbers = [str(randint(0, 100)) for i in range(n)]
with open('lesson5_task5_text.txt', 'w', encoding='utf-8') as txt:
    txt.write(' '.join(numbers))

# подсчет суммы чисел в файле
with open('lesson5_task5_text.txt', 'r', encoding='utf-8') as txt:
    content = list(map(int, txt.read().strip().split()))  # создание списка из чисел, разделенных пробелом
    print(f'Сумма чисел равна {sum(content)}')  # подсчет и вывод суммы
