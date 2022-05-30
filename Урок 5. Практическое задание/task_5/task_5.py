"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open("input.txt", "w", encoding='utf-8') as file:
    numbers = [str(num) for num in range(100)]
    text = " ".join(numbers)
    file.write(text)

with open("input.txt", "r", encoding='utf-8') as file:
    for line in file:
        numbers = [int(item) for item in line.split()]
print(sum(numbers))
