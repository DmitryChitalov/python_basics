"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

user_num = int(input("Введите номер месяца: "))

seasons = {
    '1': 'Зима',
    '2': 'Весна',
    '3': 'Лето',
    '4': 'Осень',
}

# Решение через list
list_season = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], ]

# Первый вариант (усложненный)
for el in list_season:
    exit_num = list_season.index(el) + 1
    for new_el in list_season[exit_num - 1]:
        if user_num == new_el:
            print(f"Результат через список: {seasons.get(str(exit_num))}")
            break

# Второй вариант
for el in list_season:
    exit_num = list_season.index(el)
    if user_num in list_season[exit_num]:
        print(f"Результат через список: {seasons.get(str(exit_num + 1))}")
        break

# Решение через dict
dict_season = {
    'Зима': [12, 1, 2],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11],
}


def get_season(elem):
    """ function """
    for keys, lists in dict_season.items():
        for elems in lists:
            if elem == elems:
                return keys


print(f"Результат через словарь: {get_season(user_num)}")
