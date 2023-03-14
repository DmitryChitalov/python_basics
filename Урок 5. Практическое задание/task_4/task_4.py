"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

try:
    with open("file1.txt", 'r', encoding='utf-8') as file:
        text = file.readlines()
        payrolls = []
        for line in text:
            payrolls.append(float(line.split()[1]))
            if float(line.split()[1]) < 20000:
                print(line, end='')
                # print(f'Количество слов в строке {lines.index(line)+1}: {len(line.split())}')
        # print(f'Количество слов в файле: {word_cnt}')
        print(f'Средняя зарплата сотрудников: {sum(payrolls)/len(text)}')
except IOError:
    print("Ошибка ввода-вывода!")
