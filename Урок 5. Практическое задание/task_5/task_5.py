"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

nums = '100 12 72 30 39 2 2 56 8 43 100 1 98 88 61 28 93 67 92 91'
test_file = open("test_file.txt", "w+")
test_file.write(nums)
test_file.seek(0)
content = test_file.read()
list_sum = sum([float(_) for _ in content.split(' ')])
print(list_sum)
