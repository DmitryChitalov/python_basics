# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится
# месяц(зима, весна, лето, осень). Напишите решения через list и dict.

my_year_list = ['нет такого месяца', 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer',
           'summer', 'fall', 'fall', 'fall', 'winter']
num_month = int(input("Введите номер месяца: "))
print(my_year_list[num_month])

my_year_dic = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'spring', 7: 'summer', 8: 'summer',
           9: 'summer', 10: 'fall', 11: 'fall', 12: 'winter'}
num_month = int(input("Введите номер месяца: "))
print(my_year_dic.get(num_month))
