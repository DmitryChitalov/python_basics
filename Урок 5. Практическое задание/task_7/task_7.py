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

f = "D:\TEST\\firma_7.txt"

my_list1 = []
my_dict1 = {}
k = 0  # количество строк
a = 0  # значение прибыли
try:
    with open(f) as f_obj:
        for line in f_obj:
            my_list1 = line.split()  # в список добавляю все значения текущей  строки
            x = int(my_list1[2]) - int(my_list1[3])
            if x >= 0:
                a = a + x
            k += 1
            my_dict1[my_list1[0]] = x

        my_dict1["average"] = a / k


except IOError:
    print("Произошла ошибка ввода-вывода!")

print(my_dict1)


