__author__ = 'AndreiM'
__version__ = "1.0 23.03.2023"
print("\n task_4 \n -------- \n")

number = input("Введите число: ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(f"Самая большая цифра в числе {number} - {x}")

#Ведите целое положительное число: 123456789
#Самая большая цифра в числе: 9