"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
list_of_seasons = ["зима", "весна", "лето", "осень"]
month_number = int(input("Введите номер месяца: "))
if month_number == list_of_numbers[0] or month_number == list_of_numbers[1] or month_number == list_of_numbers[11]:
    print(f"Месяц относится к времени года: {list_of_seasons[0]}")
elif month_number == list_of_numbers[2] or month_number == list_of_numbers[3] or month_number == list_of_numbers[4]:
    print(f"Месяц относится к времени года: {list_of_seasons[1]}")
elif month_number == list_of_numbers[5] or month_number == list_of_numbers[6] or month_number == list_of_numbers[7]:
    print(f"Месяц относится к времени года: {list_of_seasons[2]}")
else:
    print(f"Месяц относится к времени года: {list_of_seasons[3]}")
dict_numbers_seasons = {(1, 2, 12): "зима", (3, 4, 5): "весна", (6, 7, 8): "лето", (9, 10, 11): "осень"}
month_number_new = int(input("Введите номер месяца ещё раз: "))
for element in dict_numbers_seasons:
    for member in element:
        if member == month_number_new:
            print(f"Месяц относится к времени года: {dict_numbers_seasons[element]}")
