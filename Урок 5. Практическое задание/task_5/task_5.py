"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
in_f = open(r'D:\DevOps\Python\Урок5\test6.txt', "w")
line = "10 11 12 13"
in_f.write(line)

one, two, three, four = line.strip().split(" ")
one = float(one) # превращаем текст в число
two = float(two) # превращаем текст в число
three = float(three) # превращаем текст в число
four = float(four) # превращаем текст в число
all_summ = one + two + three + four
print(all_summ)