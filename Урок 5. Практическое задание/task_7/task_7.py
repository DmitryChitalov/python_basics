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

if __name__ == "__main__":
    results = [{}, {}]

    try:
        with open(SRC_FILENAME, encoding='utf-8') as fhs:
            lines = fhs.readlines()

        for line in lines:
            name, _, proceeds, expenses = line.split()
            results[0][name] = int(proceeds) - int(expenses)

        results[1]['average_profit'] = round(
            sum(
                profit for _, profit in results[0].items() if profit > 0
            ) / len(results[0])
        )

        with open(DST_FILENAME, "w", encoding='utf-8') as fhd:
            fhd.write(dumps(results))
    except IOError as e:
        print(e)
    except ValueError:
        print("Неконсистентные даkнные")
