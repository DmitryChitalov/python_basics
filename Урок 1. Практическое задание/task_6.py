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
while True:
    kilometer_first_day = input("Введите количество километров в первый день: ")
    try:
        kilometer_first_day = float(kilometer_first_day)
        break
    except ValueError:
        print("Введите число")
        continue
while True:
    kilometers_all = input("Введите максимальное количество километров пробежавшего пути: ")
    try:
        kilometers_all = float(kilometers_all)
        break
    except ValueError:
        print("Введите число")
        continue
count_day = 1
print("Результат: ")
print(f"1-й день: {kilometer_first_day}")
while kilometer_first_day <= kilometers_all:
    count_day += 1
    previous_day = kilometer_first_day
    kilometer_first_day += previous_day * 10 / 100
    print(f"{count_day}-й день: {'{:.2f}'.format(kilometer_first_day)}")
print(f"Ответ: на {count_day}-й день спортсмен достиг результата — не менее {kilometers_all} км.")
