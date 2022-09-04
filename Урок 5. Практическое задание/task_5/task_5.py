"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
num_obj = "1 2 3 4 5 6 7 8 9"
result = 0
with open("sum_num_file.txt", "w", encoding='utf-8') as file_obj:
    file_obj.write(num_obj)
with open("sum_num_file.txt", encoding='utf-8') as file_obj:
    content = file_obj.read().split(" ")
    for n in content:
        result = result + int(n)
    print(f"Сумма чисел = {result}")
