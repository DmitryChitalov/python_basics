"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
my_dict = {"Иванов 15000", "Петров 17000", "Сидоров 17000", "Максимов 18000",
"Протопопов 19000", "Куприянов 16000", "Мачнев 21000", "Смехов 23000", "Шкуратов 25000", "Морохов 12000",
"Набатов 9000"}
my_list_temp = []
words_n = 0
mid = 0
iteration = 0
with open("file_1.txt", "w") as out_file:
    for x in my_dict:
        out_file.writelines(x)
            #out_file.writelines(' ')
        out_file.writelines('\n')

with open("file_1.txt", "r") as my_file:
    print(my_file.read())

with open("file_1.txt", "r") as my_file:
    text_file2 = my_file.readlines()
for el in text_file2:
    words = el.split()
    for i in range(1, len(words)):
        mid += int(words[i])
        iteration +=1
        if int(words[i]) < 20000:
             my_list_temp.append(words[0])

print("Среднее значение", round(mid/iteration))
print("Зарплата меньше 20 тыс.:", end=" ")
for x in my_list_temp:
    print(x, end=', ')


