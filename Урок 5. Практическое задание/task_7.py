import json
res = {}
earning = 0
n = 0
company = {}
with open("task_7.txt", "r", encoding="utf-8") as my_f:
    for line in my_f:
        name, num, profit, loss = line.split()
        res[name] = int(profit) - int(loss)
        if res.setdefault(name) >= 0:
            earning = earning + res.setdefault(name)
            n += 1
    if n != 0:
        sum_profit = earning / n
        print(f"Average income - {sum_profit}")
    else:
        print(f"No profit")
    company = {}

with open("task_7.json", "w") as my_js:
    json.dump(sum_profit, my_js)

    json_str = json.dumps(res)
    print(f"Companies income: {json_str}")


"""
Average income - 5000.0
Companies income: {"firm_1": 5000, "firm_2": 10000, "firm_3": 0}
"""

