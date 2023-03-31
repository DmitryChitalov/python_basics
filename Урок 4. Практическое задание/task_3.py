"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генераторное выражение.

"генераторное выржаение" здесь List comprehension
"""
#!/usr/bin/env python3
magic_numbers = [20, 21]
step_number = 0

while step_number not in magic_numbers:
    step_number = int(input("Пожалуйста, выберите желаемую кратность (20 ИЛИ 21): "))

search_result = [i for i in range(step_number, 241, step_number)]
print(search_result)

no_prestidigitation = [j for j in range(20, 240) if j % 20 == 0 or j % 21 == 0]
print(f"Если без обмана, то: {no_prestidigitation}")
