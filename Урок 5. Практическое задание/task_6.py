items = {}
with open("task_6.txt", "r") as my_f:
    for line in my_f:
        name, lesson, practice, lab = line.split()
        items[name] = int(lesson) + int(practice) + int(lab)

    print(f"Result {items}")

"""
Информатика: 100 50 20
Физика: 30 0 10
Физкультура: 0 30 0

Result {'Информатика:': 170, 'Физика:': 40, 'Физкультура:': 30}
"""
