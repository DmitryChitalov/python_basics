"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генераторное выражение.
"""
def multiply(var):
    ls = [i for i in range(20, 240) if i % var == 0]
    return ls

print(multiply(20))
print(multiply(21))
# второй вариант
print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])