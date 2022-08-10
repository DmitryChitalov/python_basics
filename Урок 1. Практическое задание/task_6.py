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
a = float(input("Введите результат спортсмена в первый день, км: "))
b = float(input("Введите результат спортсмена в последний день, км: "))
if a >= b:
    print("Некорректный ввод. Результат спортсмена в последний день должен быть больше результата в первый день.")
    exit(1)
day = 1
print("Результат:")
while a < b:
    day += 1
    a = a * 1.1
    print(f"День: {day}. Расстояние: {a:.3f} км")

print(f"Ответ: на {day}-й день спортсмен достиг результата: не менее {b} км.")
