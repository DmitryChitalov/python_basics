"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

text_write = open('text_write.txt', 'w', encoding='utf-8')
text_write.write(input('Введите последовательность цифр через пробел: '))
text_write = open('text_write.txt', 'r', encoding='utf-8')
amount = 0
for number in text_write:
    number = number.split()
    for i in number:
        amount += int(i)
text_write.close()
print(f'Сумма чисел - {amount}')
