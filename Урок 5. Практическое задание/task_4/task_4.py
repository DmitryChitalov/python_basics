"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('numerals.txt', encoding='utf-8') as f_obj:
    content = f_obj.read()
    for key, value in my_dict.items():
        content = content.replace(key, value)
with open("Числительные.txt", "w", encoding='utf-8') as out_f:
    out_f.write(content)
