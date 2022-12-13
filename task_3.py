# способ 1

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autemn = [9, 10, 11]
a = int(input("Введите месяц в виде целого числа от 1 до 12: "))
for el in winter:
    if a == el:
        print('зима')
for el in spring:
    if a == el:
        print('весна')
for el in summer:
    if a == el:
        print('лето')
for el in autemn:
    if a == el:
        print('осень')

# способ 2
my_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна',6: 'лето',
           7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень',
           12: 'зима'}
a = int(input("Введите месяц в виде целого числа от 1 до 12: "))
print(my_dict.get(a))