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
my_f = open("task7_lesson5.txt", "r")
content = my_f.readlines() #извлекаем из текстового файл полный список строк
profit = {} #данная переменная будет обновляться в следующем цикле
av_profit = {}
lines = 0
lines2 = 0
divider = 0 #это счётчик цикла for. По нему мы узнаем средню прибыль
for el in content: #в данном цикле мы создаём из строки словарь, где название предмета ключ, а сумма чисел в строке -значение
    a = el.replace('ООО', '').replace('ОАО', '').replace('ЗАО', '').replace("\n", "")#убираем из очередной строки указанные символы
    b = a.split()#создаем из строки список b
    c = a.split()#создаем из строки список c
    del b[1:]#из списка "b" убираем все элементы кроме 1-го и оставляем только название фирмы
    del c[0:1]#из списка "c" убираем лишние элементы и оставляем только числа
    line = 0  # данная переменная будет обновляться в следующем цикле
    for i in range(len(c)):  # в данном цике считаем прибыль в каждой строке
        if i == 0:
           line = int(c[i]) - int(c[1])
    if line > 0: #выполняем данное условие, если нет убытка.
        lines += line
        for el in b:  #в данном цикле списко "b" переводим в строку
            b = el
        my_dict = {b: line}  #создаём словарь, где название фирмы - ключ, а cумма прибыли - значение
        divider += 1 #счётчик увеличивается на 1 при условии, если фирма прибыльная
    else: # Убытки склыдваем в переменную lines2
        lines2 += line
    profit.update(my_dict)  #объединяем все прибыльные фирмы в один словарь
    loss = {"убытки": lines2} #создаём словарь с суммой убытков
    av_profit = {"средняя прибыль": lines // divider}
print([profit, av_profit, loss])
my_f.close()
