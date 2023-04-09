subjects = {}
try:
    with open("task6.txt", encoding='utf-8') as my_f:
        li = my_f.readlines()
    for line in li:
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
except ValueError:
    print("Ошибка")

print(subjects)