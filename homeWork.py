# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.

my_var = "Hello, teacher"
print(f"I say:", my_var)

my_age = 34
print(f"How old are you?", int(my_age))

name = input("What is your name?")
print("My name is: %s, %d years old" % (name, my_age))

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты,
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input("Введите значение в секундах: "))


def hhmmss(sec):
    hours = sec // 3600
    minutes = (sec - (hours * 3600)) // 60
    print("{}:{}:{}".format(hours, minutes, sec % 60))


hhmmss(seconds)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input("Укажите число: "))


def sum_numbers(n):
    one = str(n)
    double = one + one
    trick = double + one
    print(f"{one} + {double} + {trick} =", int(one) + int(double) + int(
        trick))


sumNumbers(number)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру
# в числе. Для решения используйте цикл while и арифметические операции.

n = -1
while n < 0:
    try:
        n = int(input("Укажите любое положительное число: "))
    except ValueError:
        n = -1
array_strings = list(str(n))
if len(array_strings) > 0:
    iterate = 0
    max_number = 0
    while iterate < len(array_strings):
        next_number = int(array_strings[iterate])
        max_number = next_number if max_number < next_number else max_number
        iterate += 1
    print(f"Максимальное число = ", max_number)
print("Вычисления завершены")

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с
# каким финансовым результатом работает фирма. Например, прибыль — выручка
# больше издержек, или убыток — издержки больше выручки. Выведите
# соответствующее сообщение.
revenue = 0
costs = 0
is_set_values = False
while not is_set_values:
    try:
        revenue = int(input("Укажите сумму выручки фирмы: "))
        costs = int(input("Укажите сумму издержек фирмы: "))
        is_set_values = True
    except ValueError:
        is_set_values = False
message = "Фирма работает с прибылью" \
    if revenue > costs else "Фирма работает в убыток"
print(message)
print("Продолжение следует...")

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это
# отношение прибыли к выручке. Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.
profitability = 0

def clean_revenue(rev, cos):
    return rev - cos

def get_profitability(rev, cos):
    return clean_revenue(rev, cos) / rev

def set_employees():
    employees_count = 0
    while employees_count == 0:
        try:
            employees_count = int(input("Укажите количество сотрудников: "))
        except ValueError:
            print("Количество сотрудников не может быть меньше одного,"
                  "как минимум должен быть директор фирмы ;)")
            employees_count = 0
    return employees_count

if revenue > costs:
    profitability = get_profitability(revenue, costs)
    print("Рентабельность фирмы составляет: ", profitability)
    employees = set_employees()
    revenue_by_employee = clean_revenue(revenue, costs) / employees
    print("Прибыль на одного сотрудника составляет: ", revenue_by_employee)
print("Вычисления завершены")

# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10%
# относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров. Программа должна
# принимать значения параметров a и b и выводить одно натуральное
# число — номер дня.

def set_prompt(mes):
    km = 0
    while km == 0:
        try:
            km = int(input(mes))
        except ValueError:
            print("Спортсмен не на столько плох чтобы пробежать менее одного, "
                  "киллометра ;)")
            km = 0
    return km

def set_start():
    return int(set_prompt("Результат пробежки спортсменом в первый день"))

def set_end(start):
    b = 0
    while b <= start:
        b =  set_prompt("Финальный результат пробежки спортсменом")
        if b <= start:
            print("Финальный результат должен быть больше начального "
                  "результата!")
    return b

def race_result(start, end):
    increase = 0.1
    step_by_step = start
    result_day = 1
    while step_by_step <= end:
        step_by_step += step_by_step * increase
        result_day += 1

    print(f"Спортсмен достиг результата не менее {end} км. в день номер: "
          f" {result_day}")

a = set_start()
b = set_end(a)

race_result(a, b)
print("ДОМАШНЯЯ РАБОТА ЗАВЕРШЕНА")
