my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


def generator(my_list):
    for el in range(len(my_list) - 1):
        if  my_list[el] < my_list[el + 1]:
            yield my_list[el + 1]

for el in generator(my_list):
    result.append(el)

print(result)