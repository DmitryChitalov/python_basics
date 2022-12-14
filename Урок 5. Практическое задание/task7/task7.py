import json
my_f = open("task7.txt", "r", encoding='utf-8')
content = my_f.readline()
firm_dict = {}
average_profit_dict = {}
average_profit = 0
while content != "":
    buffer = content.split()
    profit = int(buffer[2]) - int(buffer[3])
    firm_dict[buffer[0]] = profit
    if profit >= 0:
        average_profit += profit
    content = my_f.readline()
average_profit_dict["average_profit"] = average_profit
my_list = [firm_dict, average_profit_dict]
my_f.close()
with open("task7.json", "w") as out_file:
    json.dump(my_list, out_file)