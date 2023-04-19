"""
7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json
words = []
my_dict = {}
my_dict2 = {}
value_1 = ""
sum_1 = 0
difference = 0
iteration = 0
ear = 0
average = 0
with open("test.txt", "r") as my_file:
    text_file2 = my_file.readlines()
for el in text_file2:
    words = el.split()
    difference = int(words[2]) - int(words[3])
    if difference > 0:
        ear = difference
        sum_1 = ear
        iteration += 1
    my_dict[words[0]] = ear
    ear = 0
my_dict2["average_profit"] = sum_1/iteration
print(my_dict)
print(my_dict2)
with open("file_2.json", "w") as write_f:
    json.dump(my_dict, write_f)
    write_f.write("\n")
    json.dump(my_dict2, write_f)