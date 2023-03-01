import json

def profit(revenue, costs):
    profit = int(revenue) - int(costs)
    return profit

firm_list = []
firm_dict = {}
avg_dict = {}
total_profit = 0

with open("DZ5_7.txt", 'r', encoding='utf-8') as firm_obj:
    for line in firm_obj:
        line = line.split()
        firm_dict = {line[0] : profit(line[2], line[3])}
        firm_list.append(firm_dict)

    for val in firm_dict.values():
        if val > 0:
            total_profit += int(val)
        avg_profit = total_profit / len(firm_dict.values())
        avg_dict['average_profit'] = avg_profit
        firm_list.append(avg_dict)

with open('DZ5_7.json', 'w', encoding='utf-8') as firms_json:
    json.dump(firm_list, firms_json)
