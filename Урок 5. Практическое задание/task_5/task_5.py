"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
str_obj = "1 4 7 10 15"
result = 0

with open("output_data.txt", "w", encoding='utf-8') as f_write:
    f_write.write(str_obj)

with open("output_data.txt", encoding='utf-8') as f_write:
    content = f_write.read().split(" ")
    for n in content:
        result = result + int(n)
    print(f"Сумма чисел = {result}")
