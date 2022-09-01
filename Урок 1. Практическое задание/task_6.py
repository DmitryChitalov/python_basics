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
a = int(input("Введите результат первого дня a = "))
b = int(input("Введите интересующий результат b = "))
result = a
count = 1
while result < b:
    print(f"{count}-й день: {round(result, 2)}")
    count = count + 1
    result = result * 1.1
print(f"на {count}-й день спортсмен достиг результата - не менее {b} км.")
