"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
# Flag = 1
# out_f = open('tast_1.txt', 'w', encoding='utf-8')

# while Flag == 1:
#     a = input('Введите текст: ')
#     if a == '':
#         Flag = 0
#     else:
#         out_f.writelines(f'{a} \n')

# out_f.close()

flag = 1
with open('DZ_tast_1.txt', 'w', encoding='utf-8') as out_f:
    while flag == 1:
        user_str = input('Введите текст: ')
        if user_str == '':
            flag = 0
        else:
            out_f.writelines(f'{user_str}\n')
