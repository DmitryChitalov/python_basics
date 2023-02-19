"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
# 1. Решение через dict (мне понравилось больше)
# но почему не работает так: {(12, 1, 2): 'winter'...}?

my_dict1 = {12: 'winter', 1: 'winter', 2: 'winter',
            3: 'spring', 4: 'spring', 5: 'spring',
            6: 'summer', 7: 'summer', 8: 'summer',
            9: 'autumn', 10: 'autumn', 11: 'autumn'}
print(my_dict1)
print(my_dict1.get(int(input("Введите номер месяца от 1 до 12: "))))

# Альтернативное решение 

my_dict1 = {'winter': (1, 2, 12), 'spring': (3, 4, 5),
            'summer': (6, 7, 8), 'autumn': (9, 10, 11)}
print(my_dict1)
month = int(input("Введите номер месяца от 1 до 12: "))
for key in my_dict1.keys():
    if month in my_dict1[key]:
        print(key)

# 2. Решение через list

s_list = ['winter', 'spring', 'summer', 'autumn']
n = int((input("Введите номер месяца от 1 до 12: ")))
if n == 12 or n <= 2:
    print(s_list[0])
elif n <= 5:
    print(s_list[1])
elif n <= 8:
    print(s_list[2])
elif n <= 11:
    print(s_list[3])
else:
    print("В нашем календаре такого месяца нет")
    
