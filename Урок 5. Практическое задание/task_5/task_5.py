"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

new_file = 'new_file.txt'

nums = input("Введите числа, разделенные пробелами и нажмите Enter: ")
with open(new_file, 'w', encoding='UTF-8') as fl:
    fl.write(nums)

with open(new_file, 'r', encoding='UTF-8') as num_fl:
    nums = num_fl.readline()

sum_lst = []
for elem in nums.split():
    sum_lst.append(int(elem))

print(f"Сумма введенных чисел равна {sum(sum_lst)}")
