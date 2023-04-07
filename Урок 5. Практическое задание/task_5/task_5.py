"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("text.txt", "r") as f_obj:
    while True:
        content = f_obj.readline()
        if content == "":
            break
        content_split = content.split(" ")
        result = list(map(int, content_split))
        print(f"Сумма чисел равна: {sum(result)}")
