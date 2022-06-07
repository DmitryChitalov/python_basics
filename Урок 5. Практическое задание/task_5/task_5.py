"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('text.txt', 'w+') as file:
    line = (input('enter num over space \n'))
    file.writelines(line)
    content = line.split()
    print(content)


print(sum(map(int, content)))









