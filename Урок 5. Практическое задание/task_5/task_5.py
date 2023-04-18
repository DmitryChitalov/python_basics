"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

numbers_list = [str(randint(1, 15)) for i in range(0, 10)]
print("Список чисел, записываемых в файл:")
print(" ".join(el for el in numbers_list))
with open("file.txt", "w+", encoding='utf-8') as f_obj:
    f_obj.write(' '.join(numbers_list))
    f_obj.seek(0)
    num_str = f_obj.read()
print(f"Сумма чисел в файле: {sum([int(i) for i in num_str.split()])}")
