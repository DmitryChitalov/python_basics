numerals = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}
updated = []
i = 0
with open("task_4.txt", "r", encoding="utf-8") as my_f:
    for line in my_f:
        lines = line.split(" ", 1)
        if lines[0] in numerals:
            rus = numerals[lines[0]]
            updated.append(rus + lines[1])
            i += 1
    print(updated)
with open("result.txt", "w") as my_f2:
    my_f2.writelines(updated)

"""
['один— 1\n', 'два— 2\n', 'три— 3\n', 'четыре— 4']

в файле:
один— 1
два— 2
три— 3
четыре— 4
"""
