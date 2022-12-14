from random import randint
numbers = ""
count_numbers = 0
for el in range(10):
    numbers = numbers + str(randint(1, 40)) + " "
numbers = numbers[0:len(numbers) - 1]
my_f = open("task5.txt", "w", encoding='utf-8')
my_f.writelines(numbers)
my_f.close()
my_f = open("task5.txt", "r", encoding='utf-8')
numbers = my_f.readlines()
numbers = numbers[0].split()
for el in range(len(numbers)):
    count_numbers = count_numbers + int(numbers[el])
print(count_numbers)
my_f.close()