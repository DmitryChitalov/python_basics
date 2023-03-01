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
file_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_3/my_data.txt'
new_file_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_3/new_my_data.txt'

my_dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

def my_func(file):
    my_data = []
    new_my_data = []
    with open(file, 'r', encoding='utf-8') as file:
        my_data = file.read().split('\n')
    for el in my_data:
        for key in my_dictionary:
           test = el
           if key in test:
               new_my_data.append(test.replace(key, my_dictionary[key]))
    with open(new_file_name_and_path, 'w', encoding='utf-8') as file:
        file.writelines('%s\n' % line for line in new_my_data)      
        
my_func(file_name_and_path)

