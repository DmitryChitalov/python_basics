"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


new_list = []
while True:
    line = input("Enter digits: ")
    if line == '':
        print(new_list)
        exit()
    else:
        newline = str(line)
        new_list.append(newline)

    with open("text.txt", "w") as file_obj:
        file_obj.writelines(new_list)
        #print(new_list)
