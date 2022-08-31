"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
my_write_file = open("my_new_file.txt", "w")
my_write_file.write("654 321 564 987 654 321 654 987 654 321 654 987 354 984")
my_write_file.close()

my_read_file = open("my_new_file.txt", "r")
text_from_file = my_read_file.read()
total = 0
for elem in text_from_file.split(" "):
    total += int(elem)
my_read_file.close()
print("Сумма всех чисел: ", total)
