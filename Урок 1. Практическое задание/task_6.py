
__author__ = 'Юлия Павлова'
__group__ = 2547

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
a = int(input('Введите результаты пробежки в км/ч в первый день:'))
b = int(input('Введите желаемый результат в км/ч:'))
day_result = 1
km_result = a
while km_result < b:
    a = a * 0.1 + a
    day_result +=1
    km_result = km_result + 1
print(f'Спортсмен достигнет результата на {day_result} день.')
