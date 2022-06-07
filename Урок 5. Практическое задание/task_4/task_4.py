"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
sal = []
worker = []
with open('file.txt') as f_file:
    content = f_file.read().split('\n')
    print(content)
    for i in content:
        i = i.split()
        print(i)
        if int(i[1]) < 20000:
            worker.append(i[0])
        sal.append(int(i[1]))
print(worker)
print(sum(sal) / len(sal))




