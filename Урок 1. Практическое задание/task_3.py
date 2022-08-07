"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

# Приветственное сообщение
print("Программа нахождения суммы чисел n + nn + nnn.\n")

# Создадим функцию ввода числа и проверки типа
def input_and_check_num(text):
    temp_in = input(text)
    while True:
        try:
            temp_in = abs(int(temp_in))%10
            return temp_in

        except Exception:
            print('Введите целое число ')
            temp_in = input()
            continue

# Для корректной работы цикла, объявляем переменную
temp_number = 1

while temp_number != 0:
    # Ввод исходных данных
    temp_number = input_and_check_num("Введите значение числа n от 1 до 9 (0-завершение программы): ")
    if temp_number == 0:
        break
    duble_temp_number = temp_number * 11
    triple_temp_number = temp_number * 111

    # Вывод результата на экран
    print(f"При исходном значении n={temp_number} \n"
          f"Результат:\n"
          f"{temp_number} + {duble_temp_number} + {triple_temp_number} = ", temp_number + duble_temp_number + triple_temp_number)