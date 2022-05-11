import json

with open("text3.json", encoding='1251') as f:
    my_dict = json.load(f)
    print("Сотрудники, зарабатывающие менее  20000$ в год:")
    for keys, values in my_dict.items():
        if values < 20000:
            print(keys)
    print(f"Средняя заработная плата = {sum(my_dict.values())/len(my_dict)} $ в год")
