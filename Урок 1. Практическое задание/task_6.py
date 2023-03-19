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

a = float(input("Введите результаты пробежки первого дня в км "))
b = float(input("Введите общий желаемый результат в км "))
result_days = 1
while a < b:
        print("%d-й день: %.2f" % (result_days,a))
        a = a + 0.1 * a
        result_days += 1
print("%d-й день: %.2f" % (result_days,a))
print("Ответ: на %d-й день спортсмен достиг результата — не менее %.2f км." % (result_days,a))
