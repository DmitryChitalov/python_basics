"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
word_count_dict = {}
my_rows_count = 0
my_total = 0

with open("my_file05_04.txt", "r", encoding='UTF8') as my_file:
    for my_row in my_file:
        my_words = my_row.split(" ")

        my_rows_count += 1
        my_total += float(my_words[1])

        if float(my_words[1]) < 20000:
            word_count_dict[my_words[0]] = my_words[1].replace('\n', '')

my_middle = my_total / my_rows_count


for my_info in word_count_dict.items():
    print(f"Работник {my_info[0]} получает {my_info[1]} денег.")

print(f"\nСредний заработок: {my_middle} денег")
