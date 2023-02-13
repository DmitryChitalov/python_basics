f_6 = open("file_6.txt", "r", encoding='utf-8')
lines = f_6.readlines()
f_6.close()
my_dict = {}
for line in lines:
    total = 0
    name, lessons = line.split(":")
    lesson = lessons.split()
    for l in lesson:
        hours, o = l.split("(")
        total += int(hours)
    my_dict.update({name: total})
print(my_dict)