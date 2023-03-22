__author__ = 'AndreiM'
__version__ = "1.0 23.03.2023"
print("\n task_3 \n -------- \n")

n = int(input("Введите число n: "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(f"n + nn + nnn = {n} + {n}{n} + {n}{n}{n} = {total}")

#Введите число n: 3
#n + nn + nnn = 369