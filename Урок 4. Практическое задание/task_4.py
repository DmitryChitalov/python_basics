from random import randint

lenght = int(input("Введите длинну исходного списка "))
my_string = [randint(0, 20) for el in range(0, lenght)]
print(my_string)
new_string = [el for el in my_string if my_string.count(el) == 1]
print(new_string)
