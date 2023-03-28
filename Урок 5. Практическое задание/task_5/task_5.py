"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

a = open('text5.txt', 'w', encoding='UTF-8')
text = input("Введите данные: ").split()
a.writelines(text)

for i in range(len(text)):
    text[i] = int(text[i])
print(text)
print(sum(text))
a.close()
