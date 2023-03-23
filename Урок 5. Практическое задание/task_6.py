with open("task6.txt", "r", encoding='utf-8') as file:
    subjects_dict = {}
    for line in file:
        subject, *lessons = line.strip().split(", ")
        total_lessons = sum(int(x.split(" - ")[1]) for x in lessons)
        subjects_dict[subject] = total_lessons

print(subjects_dict)
