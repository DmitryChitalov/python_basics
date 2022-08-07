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
first_name = 'empty1'
string_one = 'empty2'
first_number = 1
second_number = 2
other_number = 3
soul_number = 23435459
count_numbers = 8

# Приветственное сообщение
print("Программа генерации пары логин-пароль\n\n")

# Создадим функцию ввода числа и проверки типа
def input_and_check_num(text):
    temp_in = input(text)
    while True:
        try:
            temp_in = int(temp_in)
            return temp_in

        except Exception:
            print('Введите целое число ')
            temp_in = input()
            continue

# Вводим данные
first_name = input("Введите имя: ")
first_number = input_and_check_num("Введите первое число: ")
second_number = input_and_check_num("Введите второе число: ")

# Генерируем пароль из чисел
other_number = ((first_number * soul_number + soul_number) % (10 ** count_numbers) + (second_number * soul_number + soul_number) % (10 ** count_numbers)) % (10 ** count_numbers)

# Вывод данных на экран
print(f"Для входа в учетную запись введите \n"
      f"Логин: {first_name} \n"
      f"Пароль: {other_number}")