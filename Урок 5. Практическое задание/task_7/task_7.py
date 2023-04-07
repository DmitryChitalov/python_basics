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

with open("text.txt", "r", encoding="utf-8") as f_obj:
    profit_sum = 0
    company_dict = {}
    profit_average = {}
    result = []
    sum_profit = 0
    count_company = 0
    while True:
        content = f_obj.readline()
        if content == "":
            break
        name = content.split(" ", 1)[0]
        content_split = content.split("   ")
        content_split = [line.rstrip() for line in content_split]
        content_numbers_split = [content_split[el] for el in range(2, len(content_split))]
        content_numbers = list(map(int, content_numbers_split))
        profit = content_numbers[0] - content_numbers[1]
        company_dict[name] = profit
        if profit > 0:
            sum_profit += profit
            count_company += 1
    profit_average = {"average_profit": sum_profit / count_company}
    result = [company_dict, profit_average]

    with open("text.json", "w", encoding="utf-8") as json_txt:
        json.dump(result, json_txt, ensure_ascii=False)
