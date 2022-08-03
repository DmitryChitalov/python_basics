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
passed_1 = int(input("Введите, пожалуйста, количество километров за 1 день: "))
passed_n = int(input("Введите, пожалуйста, целевое количество километров: "))
day_n = 1

while passed_1 <= passed_n:
    print(f"{day_n}-й день: {passed_1}")
    if passed_1 >= passed_n:
        break
    else:
        day_n += 1
        passed_1 = round(passed_1 + (passed_1 / 100 * 10), 1)
print(f"На {day_n}-й день спортсмен достиг результата - не менее {passed_n} км")
