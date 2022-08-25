"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
new = []
my_var = 0
score = 0
my_text = input("Введите текст в файл: ")
with open('test.txt', 'w', encoding='utf-8') as my_f:
    while my_text != '':
        my_f.writelines(my_text + '\n')
        my_text = input()

with open('test.txt', 'r', encoding='utf-8') as f_obj:
    content = f_obj.readlines()

for i in content:
    new.append(i.split())

print("Сотрудники чей оклад меньше 20 000:")
for i in new:
    i[1] = int(i[1])
    if i[1] < 20000:
        print(i[0])
    my_var += i[1]
    score += 1
my_var = my_var / score

print(f'Средний заработок сотудников состовляет {my_var}')




