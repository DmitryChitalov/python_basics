# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую неотрицательную степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def toDegree(a, b):
    if b < 0:
        return print('Error')
    return a ** b
a = int(input())
b = int(input())
print(toDegree(a, b))