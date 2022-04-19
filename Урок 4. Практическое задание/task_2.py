from random import randint

lenght = int(input("Введите длинну исходного списка "))
my_string = [randint(0, 20) for el in range(0, lenght)]
rez = []
print(f"исходный список - {my_string}")
for el in range(1, len(my_string)):
    if my_string[el] > my_string[el - 1]:
        rez.append(my_string[el])
print(f"результат без включения - {rez}")

rez2 = [my_string[el] for el in range(1, len(my_string)) if my_string[el] > my_string[el - 1]]
print(f"результат с использованием включения - {rez2}")
