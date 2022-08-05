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
def inputandchecknum (text):
    tempin = input (text)
    while True:
        try:
            tempin = abs (int(tempin))%10
            return tempin

        except Exception:
            print('Введите целое число ')
            tempin = input()
            continue

# Для корректной работы цикла, объявляем переменную
tempnumber = 1

while tempnumber != 0:
    # Ввод исходных данных
    tempnumber = inputandchecknum("Введите значение числа n от 1 до 9 (0-завершение программы): ")
    dubletempnumber = str (tempnumber) + str (tempnumber)
    tripletempnumber = str (tempnumber) + str (tempnumber) + str (tempnumber)

    # Вывод результата на экран
    print(f"При исходном значении n={tempnumber} \n"
          f"Результат:\n"
          f"{tempnumber} + {dubletempnumber} + {tripletempnumber} = ", tempnumber + int(dubletempnumber)+int(tripletempnumber))
