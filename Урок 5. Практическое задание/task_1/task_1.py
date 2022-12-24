"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_file = 'my_text.txt'

while True:
    user_text = input("Введите текст, а я буду писать в файл...: ")
    with open(new_file, 'a', encoding="UTF-8") as open_file:
        if user_text.lower() == 'stop':
            break
        print(user_text, file=open_file, end='\n')
        print('Если не хотите больше печатать - введите слово "STOP"')

print('Закончили...')
with open(new_file, 'r', encoding='UTF-8') as file:
    print('Вот содержание твоего файла:')
    print(file.read())
