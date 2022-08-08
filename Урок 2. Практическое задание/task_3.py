"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month = int(input("Please enter month number:"))                            # Ask for input from a user
while not 1 <= month <= 12:                                               # Chech if number is in range from 1 to 12
    month = int(input("Please enter month number between 1 and 12:"))       # If the number is not in the range, keep asking for proper number


year_list=[                                                                 # Create a list of Seasons
    None,                                                                   # None item to map index to value 1 to 1
    "Winter","Winter","Spring",
    "Spring","Spring","Summer",
    "Summer","Summer","Autumn",
    "Autumn","Autumn","Winter"]

print(year_list[month])                                                     # Print item from the seasons list by the index


# Find the season by using dictionary

year_dict = {                                                               # Create dictionary with months and seasons
    "Winter":[12,1,2],
    "Spring":[3,4,5], 
    "Summer":[6,7,8], 
    "Autumn":[9,10,11]}

for key,value in year_dict.items():                                         # If the month is in the value of the key, print key
    if month in value:
        print(key)