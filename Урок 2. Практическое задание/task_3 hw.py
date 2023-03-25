__author__ = 'AndreiM'
__version__ = "1.0 24.03.2023"
print("\n task_3 \n -------- \n")

month = int(input("Введите месяц в виде целого числа: "))
seas_list = ['Зима', 'Весна', 'Лето', 'Осень']
seas_dict = {1: 'Зима',
             2: 'Весна',
             3: 'Лето',
             4: 'Осень'}
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if month == 1 or month == 2 or month == 12:
    print(f"Результат через словарь dict: {seas_dict.get(1)}. Месяц: {month_list[month - 1]} ({month})")
    print(f"Результат через список list: {seas_list[0]}. Месяц: {month_list[month - 1]} ({month})")
elif month == 3 or month == 4 or month ==5:
    print(f"Результат через словарь dict: {seas_dict.get(2)}. Месяц: {month_list[month - 1]} ({month})")
    print(f"Результат через список list: {seas_list[1]}. Месяц: {month_list[month - 1]} ({month})")
elif month == 6 or month == 7 or month == 8:
    print(f"Результат через словарь dict: {seas_dict.get(3)}. Месяц: {month_list[month - 1]} ({month})")
    print(f"Результат через список list: {seas_list[2]}. Месяц:  {month_list[month - 1]} ({month})")
elif month == 9 or month == 10 or month == 11:
    print(f"Результат через словарь dict: {seas_dict.get(4)}. Месяц: {month_list[month - 1]} ({month})")
    print(f"Результат через список list: {seas_list[3]}. Месяц: {month_list[month - 1]} ({month})")
else:
    print("Такого месяца не существует. Введите целое число от 1-12")


"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""