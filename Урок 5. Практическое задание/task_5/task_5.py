"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open("lesson5-5.txt", "w") as num:
    line = input("Запишите набор цифр через пробел: ")
    num.writelines(line)
resoult = 0
with open("lesson5-4.txt", "r") as new_file:
    same_list = new_file.read()
    for num in same_list.split():
        resoult = resoult + int(num)
    print(resoult)

