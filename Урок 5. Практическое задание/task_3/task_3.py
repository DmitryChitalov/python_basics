"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
my_list_temp = []
words_n = 0
with open("file_3.txt", "r") as my_file:
    text_file = my_file.readlines()
for j in text_file:
    words = j.split()
    words_n += len(words)
print("Количество слов: ", words_n)
with open("file_3.txt", "r") as my_file:
    text_file2 = my_file.readlines()
for el in text_file2:
    words = el.split()
    for i in range(len(words)):
        for my_key in my_dict.keys():
            if words[i] == my_key:
                words[i] = my_dict[my_key]
                break
    my_list_temp.append(words)
with open("file_3.2.txt", "w") as out_file:
    for x in my_list_temp:
        for y in x:
            out_file.writelines(y)
            out_file.writelines(' ')
        out_file.writelines('\n')

with open("file_3.2.txt", "r") as my_file:
    print(my_file.read())
