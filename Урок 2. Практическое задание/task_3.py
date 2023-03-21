"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

season_list = ['зима', 'весна', 'лето', 'осень']
wr = season_list[0]
sp = season_list[1]
sr = season_list[2]
ot = season_list[3]
season_dict = {1: wr, 2: wr, 3: sp, 4: sp, 5: sp, 6: sr, 7: sr, 8: sr, 9: ot, 10: ot, 11: ot, 12: wr}
month = int(input("Введите номер месяца от 1 до 12:"))

if month > 12 or month < 1:  # проверка корректности введенных данных
    print("Введен некорректный номер.")
    season_list_res = "Невозможно определить."
    season_dict_res = "Невозможно определить."
else:
    season_dict_res = season_dict.get(month)
    if (month >= 3) and (month <= 5):
        season_list_res = season_list[1]
    elif (month >= 6) and (month <= 8):
        season_list_res = season_list[2]
    elif (month >= 9) and (month <= 11):
        season_list_res = season_list[3]
    else:
        season_list_res = season_list[0]
print("Результат через список:", season_list_res)
print("Результат через словарь:", season_dict_res)
