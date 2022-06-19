"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
chislo = input("Введите число месяца ===>   ")
# исключение, что бы не ввели символы
try:
    chislo = int(chislo)
    print("Месяц введен верно")
except ValueError:
    print("Не верный формат ввода")
if chislo > 12:
    print("Не верно введено число")
else:
    pora = ["Зима", "Весна", "Лето", "Осень"]
    if chislo <= 5 or chislo == 12:
        if chislo <= 2 or chislo == 12:
            print((chislo), "явлеяется месяцем", pora[0])
        else:
            print((chislo), "явлеяется месяцем", pora[1])
    else:
        if chislo <= 8:
            print((chislo), "явлеяется месяцем", pora[2])
        else:
            print((chislo), "явлеяется месяцем", pora[3])
    # часть с словарями
    pora = {1: "Зима", 2: "Весня", 3: "Лето", 4: "Оень"}
    if chislo <= 5 or chislo == 12:
        if chislo <= 2 or chislo == 12:
            print((chislo), "явлеяется месяцем", pora.get(1))
        else:
            print((chislo), "явлеяется месяцем", pora.get(2))
    else:
        if chislo <= 8:
            print((chislo), "явлеяется месяцем", pora.get(3))
        else:
            print((chislo), "явлеяется месяцем", pora.get(4))
