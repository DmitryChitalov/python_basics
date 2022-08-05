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
def inputandchecknum (text):
    tempin = input (text)
    while True:
        try:
            tempin = abs (int(tempin))
            return tempin

        except Exception:
            print('Введите целое число ')
            tempin = input()
            continue

# Вводим исходное число
fullnum = inputandchecknum("Введите целое число: ")

# Выполняем математические операции
fullnum = str (fullnum)
maxdigit = int (0)
indexstring = 0
for i in fullnum:
    tempnum = int (fullnum[indexstring])
    if tempnum == 9:
        maxdigit = tempnum
        break
    if tempnum > maxdigit:
        maxdigit = tempnum
    indexstring = indexstring + 1

# Выводим результат на экран
print(f"Максимальная цифра в числе {fullnum} - {maxdigit}")