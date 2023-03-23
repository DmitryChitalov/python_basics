"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
"""

a = int(input("Введите результат в первый день в км.: "))
b = int(input("Введите требуемый результат в км.: "))
day = 1
print("Результат: ")
print(f"{day}-й день: ", a)
while a < b:
    a *= 1.1
    day += 1
    print(f"{day}-й день: ", round(a, 2))
else:
    print(f"Ответ: на {day}-й день спортсмен достиг результата - не менее {b} км")
