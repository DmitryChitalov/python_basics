"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
out_f = open('out_file.txt', 'w', encoding='utf-8')
while True:
    str_list = [input('Введите данные, для окончания ввода введите пустую строку:\n')]
    if str_list[-1] == '':
        print('Ввод окончен')
        break
    for i in range(len(str_list)):
        out_f.writelines(f'\n {str_list[i]}')
out_f.close()
