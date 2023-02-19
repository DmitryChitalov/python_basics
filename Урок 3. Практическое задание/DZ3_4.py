# Способ № 1
def my_func_1(x, y):
   return x ** y
print(f' Первый способ: {my_func_1(float(input("Возводимое в степень число Х: ")), int(input("Показатель степени Y (отрицательное число): ")))}')

# Способ № 2

def my_func_2(x, y):
   i = 1
   my_res = 1 / x
   while i < abs(y):
      my_res = my_res * (1 / x)
      i += 1
   return my_res
print(f' Второй способ способ: {my_func_2(float(input("Возводимое в степень число Х: ")), int(input("Показатель степени Y (отрицательное число): ")))}')