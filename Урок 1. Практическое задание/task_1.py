"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
# Зададим переменные заранее
firstname = str ('empty1')
stringone = str ('empty2')
firstnumber = int (1)
secondnumber = int (2)
othernumber = int (3)
soulnumber = int (23435459)
countnumbers = int (8)

# Приветственное сообщение
print("Программа генерации пары логин-пароль\n\n")

# Создадим функцию ввода числа и проверки типа
def inputandchecknum (text):
    tempin = input (text)
    while True:
        try:
            tempin = int(tempin)
            return tempin

        except Exception:
            print('Введите целое число ')
            tempin = input()
            continue

# Вводим данные
firstname = input("Введите имя: ")
firstnumber = inputandchecknum("Введите первое число: ")
secondnumber = inputandchecknum("Введите второе число: ")

# Генерируем пароль из чисел
othernumber = ((firstnumber * soulnumber + soulnumber) % (10 ** countnumbers) + (secondnumber * soulnumber + soulnumber) % (10 ** countnumbers)) % (10 ** countnumbers)

# Вывод данных на экран
print(f"Для входа в учетную запись введите \n"
      f"Логин: {firstname} \n"
      f"Пароль: {othernumber}")