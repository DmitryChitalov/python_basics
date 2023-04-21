__author__ = 'AndreiM'
__version__ = "1.0 18.04.2023"
print("\n task_4 \n -------- \n")

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

filename = 'text_4.txt'
'''
Иванов 10000.0
Петров 15000.0
Сидоров 25000.1
Иванова 15000.7
Петрова 19000.9
Сидорова 26000.1
Петровский 26000.4
Знаменский 12000.0
'''


try:
    with open(filename, 'r', encoding='utf-8') as my_text:
        sal = []
        minsal = []
        my_list = my_text.read().split('\n')
        for i in my_list:
            i = i.split()
            if float(i[1]) < 20000:
                minsal.append(i[0])
            sal.append(i[1])
    print(f'  Оклад менее 20.000 у {len(minsal)} сотрудников: {minsal}  \n  Cредний оклад всех {len(my_list)} сотрудников: {sum(map(float, sal)) / len(sal)}')

except FileNotFoundError:
    print(f'Error. Невозможно открыть файл')


filename = 'text_4.txt'

def summ():
    try:
        with open(filename, 'w+', encoding='utf-8') as f:
            line = input('Введите числа через пробел:   ')
            f.writelines(line)
            numb = line.split()
            print(sum(map(float, numb)))
    except IOError:
        print('Error. Невозможно создать файл')
    except ValueError:
        print('Вы ввели недопустимый формат. Необходимо вводить только числа!')
summ()
Footer
