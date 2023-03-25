"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генераторное выражение.

"генераторное выржаение" здесь List comprehension
"""
#!/usr/bin/env python3
step_input = int(input("Пожалуйста, выберите желаемую кратность (20 или 21): "))
search_result = [i for i in range(step_input, 241, step_input)]
print(search_result)

