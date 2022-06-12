my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
elem = my_list[9]
print(elem)
my_list = ["зима", "весна", "лето", "осень"]
elem = my_list[3]
print(elem)

my_dict = {'зима': 1, 'весна': 3, 'лето': 8, 'осень': 10}
print(sorted(my_dict, key=my_dict.get))

