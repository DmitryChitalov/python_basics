"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
num_in_file = "50 10 70 20 5 100" # 255
result = 0

with open("file_task_5.txt", "w", encoding='utf-8') as f_obj:
    f_obj.write(num_in_file)

with open("file_task_5.txt", encoding='utf-8') as f_obj:
    items = f_obj.read().split(" ")
    for i in items:
        result = result + int(i)
    print(f"Сумма = {result}")
