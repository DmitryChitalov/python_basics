"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

number = int(input("Введите номер месяца:"))
list = ["зима", "весна", "лето", "осень"]
while True:
    if number == 12 or (number >= 1 and number < 3):
        print(f"Результат через список: {list[0]}")
        break
    elif number >= 3 and number < 6:
        print(f"Результат через список: {list[1]}")
        break
    elif number >= 6 and number < 9:
        print(f"Результат через список: {list[2]}")
        break
    elif number >= 9 and number < 12:
        print(f"Результат через список: {list[3]}")
        break
    else:
        print ("Несуществующие значение")
        break
    
season = {
    1: "зима", 2: "весна", 
    3: "лето", 4: "осень"
    }

dictionary = {
    1: season.get(1), 2: season.get(1), 
    3: season.get(2), 4: season.get(2), 
    5: season.get(2), 6: season.get(3), 
    7: season.get(3), 8: season.get(3), 
    9: season.get(4), 10: season.get(4),
    11: season.get(4), 12: season.get(1)
    }

answer = dictionary[number] if number in dictionary else print(f"Несуществующие значение")
print(f"Результат через словарь: {answer}")
