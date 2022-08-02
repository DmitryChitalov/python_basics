"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

user_val = input("Введите целое положительное число: ")
if user_val == "0":
  print('Ноль не является положительным числом')
else:
  try:
    user_val = int(user_val)
    if user_val < 1:
      print('Введенное число не положительное')
    else:
      print(f'Результат контакенации: {str(user_val) + str(user_val * 2) + str(user_val * 3)}')
      print(f'Результат сложения: {user_val + user_val * 2 + user_val * 3}')       
  except ValueError:
    print('Введенное число не является целым')
