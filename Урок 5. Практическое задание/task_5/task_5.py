"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
with open("number.txt", 'w', encoding='utf-8') as f_obj:
    f_obj.write("11 22 121 4343 434 54 653")

with open("number.txt", 'r', encoding='utf-8') as f_obj:
    print(sum(int(number) for number in f_obj.readline().split()))
