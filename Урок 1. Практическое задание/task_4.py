#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number_user = int(input("Введите целое положительное число: "))
number_big = 0
while number_user  != 0:
    last_number = number_user  % 10
    if last_number > number_big:
        number_big = last_number
    number_user  //= 10
print("Мы нашли самую большую цифру в числе: ", number_big)