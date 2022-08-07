"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

# Приветственное сообщение
print("Программа нахождения наибольшей цифры в целом числе.\n")

# Создадим функцию ввода числа и проверки типа
def input_and_check_num(text):
    temp_in = input(text)
    while True:
        try:
            temp_in = abs(int(temp_in))
            return temp_in

        except Exception:
            print('Введите целое число ')
            temp_in = input()
            continue

# Вводим исходное число
full_num = input_and_check_num("Введите целое число: ")

# Выполняем математические операции
full_num = str(full_num)
max_digit = 0
index_string = 0
for i in full_num:
    temp_num = int(full_num[index_string])
    if temp_num == 9:
        max_digit = temp_num
        break
    if temp_num > max_digit:
        max_digit = temp_num
    index_string = index_string + 1

# Выводим результат на экран
print(f"Максимальная цифра в числе {full_num} - {max_digit}")