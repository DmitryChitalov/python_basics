"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генераторное выражение.
"""
if __name__ == '__main__':
    result = (i for i in range(20, 241) if not i % 20 or not i % 21)

    print(f"Is generator object: {result.__class__.__name__ == 'generator'}")
    print(list(result))
