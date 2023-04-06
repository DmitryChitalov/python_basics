"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("file.txt", "w", encoding='utf=8') as f_obj:
    for i in range(1, 100):
        f_obj.write(str(i) + " ")

my_sum = 0
with open("file.txt", encoding='utf=8') as f_obj:
    content = f_obj.read()
    print(content)
    for el in content.split():
        my_sum += int(el)
    print(f"Сумма чисел в файле {my_sum}")
