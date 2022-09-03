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

with open("data_file7.txt", "r", encoding="UTF-8") as df:
    txt = df.read()
    df.seek(0)
    result = []
    revenue = {}
    summ = 0
    for line in df:
        el = line.split(" ")
        profit = int(el[2]) - int(el[3])
        if profit > 0:
            revenue.update({el[0]: profit})
            summ += profit
    result.append(revenue)
    result.append({"average_profit": (summ / len(revenue))})

with open("task07.json.tmp", "w", encoding="UTF-8") as jsf:
    json.dump(result, jsf, ensure_ascii=False)

js_object = json.dumps(result, ensure_ascii=False)

print(f"\nСловарь средней прибыли:\n{result}")
print(f"\njson-объект:\n{js_object}")