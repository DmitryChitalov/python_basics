def sum_in_line(line):
    res = 0
    for el in line.split():
        try:
            res += int(el)
        except ValueError:
            pass
    return res

key_list = []
with open("subjects", "r") as file:
    for line in file:
        key_list.append(line.split()[0])    
print(key_list)
lessons = []
with open("subjects", "r") as file:
    for line in file:
        lessons.append((sum_in_line(line)))
subj_dict = dict(zip(key_list, lessons))
print(subj_dict)
