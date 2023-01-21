"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

var_of_number_1 = int(input("Пользователь! Введите число n! : "))

amount_of_numbers = (var_of_number_1 + (var_of_number_1 + var_of_number_1 * 10)
                     + (var_of_number_1 + var_of_number_1 * 10 + var_of_number_1 * 100))
print(f"Сумма чисел n + nn + nnn равна: {amount_of_numbers}")
