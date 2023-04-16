"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генераторное выражение.
"""


def find_multiples_of_numbers(start_number, end_number):
    return [i for i in range(start_number, end_number + 1) if i % 20 == 0 or i % 21 == 0]

if __name__ == "__main__":
    print(find_multiples_of_numbers(20, 240))
