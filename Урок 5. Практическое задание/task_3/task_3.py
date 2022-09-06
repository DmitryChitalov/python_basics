"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

# Определяем функцию проверки слова
def __check_world(text):
    world_list = {'One': 'Один',
                  'Two': 'Два',
                  'Three': 'Три',
                  'Four': 'Четыре'}
    try:
        text_out = world_list[text]
    except KeyError:
        text_out = text
    return text_out


# Выводим задание для программы
print(f'\nНеобходимо написать программу, открывающую файл на чтение и считывающую построчно данные.\n'
      f'При этом английские числительные должны заменяться на русские.\n'
      f'Новый блок строк должен записываться в новый текстовый файл.\n')

# Открываем файлы ввода и вывода
input_file = open('first_file.txt', encoding="utf-8")
output_file = open('second_file.txt', 'w', encoding="utf-8")


# Проверяем слова в файле
for line in input_file:
    list_of_element = line.split()
    for el in list_of_element:
        print(f'{__check_world(el)} ', file=output_file, end='')
    print('', file=output_file)

# Закрываем файлы
input_file.close()
output_file.close()
