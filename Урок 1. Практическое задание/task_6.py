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

input_start_result = input("Please, input start value: ")
input_current_result = input("Please, input current result: ")
if str.isdigit(input_start_result) & str.isdigit(input_current_result):
    start_result = int(input_start_result)
    current_result = int(input_current_result)
    iterator = 0
    progress_ratio = 0.1
    day_result = start_result

    while(day_result < current_result):
        print(f"Day {iterator + 1}: {day_result}")
        day_result = day_result + day_result * progress_ratio
        iterator += 1
    
    print(f"On day {iterator + 1} the athlete reached the result of {current_result} km")
else:
    print("Error: start and current result not is integer value")

input()