import json

with open("task7_notprog.txt", "r", encoding='utf-8') as f_obj:
    content = f_obj.read().split('\n')
    prof = []
    res_list = []
    dict_prof = {}
    dict_mean = {}
    for line in content:
        line = line.split(' ')
        firm = line[0]
        earn = int(line[2])
        costs = int(line[3])
        profit = earn - costs
        print(f"Прибыль {firm} равна {profit}")
        prof.append(profit)
        if profit >= 0:
            sum_prof = sum(map(int, prof))
            mean_prof = sum_prof / len(prof)
        dict_prof[firm] = profit
        dict_mean = {'mean_profit': mean_prof}
    res_list.append(dict_prof)
    res_list.append(dict_mean)

with open("task7.json", "w") as write_f:
    json.dump(res_list, write_f)
