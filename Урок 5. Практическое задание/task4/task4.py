translation = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
my_f = open("text.txt", "r", encoding='utf-8')
new_content = []
new_file = []
content = my_f.readline()
while content != "":
    new_content = content.split()
    new_content[0] = translation[new_content[0]]
    content = my_f.readline()
    new_file.append(" ".join(new_content) + "\n")
my_f.close()
new_text = open("new_text.txt", "w", encoding='utf-8')
new_text.writelines(new_file)
new_text.close()