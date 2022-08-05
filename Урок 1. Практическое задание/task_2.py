"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
# Приветственное сообщение
print("Программа перевода секунд в формат ЧЧ:ММ:СС\n\n")

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

# Для корректной работы цикла, объявляем переменную
insec = 1

while insec != 0:
    # Ввод исходных данных
    insec = inputandchecknum("Введите значение секунд для преобразования (0-завершение программы): ")

    # Арифметические преобразования и цикл
    calchours = insec // (60 * 60)
    calcminuts = (insec - ( calchours * 60 * 60 ))//60
    calcsec = insec - calcminuts * 60 - calchours * 60 * 60

    # Вывод результата на экран
    print ( f"В {insec} секундах {calchours} часов {calcminuts} минут {calcsec} секунд")
    