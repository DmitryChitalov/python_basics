"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

new_file = open('text1.txt', 'w')
words = input('Введите текст (для остановки - пустая строка) \n')
while words:
    new_file.writelines(words)
    words = input('Введите текст (для остановки - пустая строка) \n')
    if not words:
        break

new_file.close()
new_file = open('text1.txt', 'r')
finaly_content = new_file.readlines()
print(finaly_content)
new_file.close()