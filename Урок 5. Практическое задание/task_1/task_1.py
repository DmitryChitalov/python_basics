"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_obj = open("my_file_txt", 'w', encoding='utf-8')
my_list = []
while True:
    line = input("Введите данные или нажмите Enter для завершения: ")
    if line != '':
        my_list.append(line + "\n")
    else:
        break
my_obj.writelines(my_list)
with open("my_file_txt", "r", encoding='utf-8') as my_obj:
    content = my_obj.readlines()
    print(content)
with open("my_file_txt", "r", encoding='utf-8') as my_obj:
    for my_list in my_obj:
        print(my_list)
