numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

items = [x for x in numbers if numbers.count(x) == 1]

print(items)