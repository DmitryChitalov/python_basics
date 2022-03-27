"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

"""ФИО Суслин Александр"""

first_day_result = float(input("Enter first day result: "))
desired_result = float(input("Enter desired result: "))

if 0 >= first_day_result or 0 >= desired_result:
    print("Invalid first_day_result or desired_result.")
    exit()

new_distance = first_day_result
day_count = 1

while new_distance < desired_result:
    new_distance = new_distance + (new_distance / 100) * 10
    day_count += 1

print(f"{day_count} day")
