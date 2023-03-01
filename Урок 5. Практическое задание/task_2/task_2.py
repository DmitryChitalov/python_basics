"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file_name_and_path = '/Users/aleksandr_bolokhov/Desktop/GeekBrains/DevOps/Python/homeworks/python_basics/Урок 5. Практическое задание/task_2/my_data.txt'
  
try:
    with open(file_name_and_path, 'r', encoding='utf-8') as file:
        my_data = file.readlines()
        print(f'Количество строк: {len(my_data)}')
        for index, words_line in enumerate(my_data):
            print(f'Строка: {index + 1}, количество слов: {len(words_line.split())}')
except IOError:
    print('Что-то пошло не так!')
    
