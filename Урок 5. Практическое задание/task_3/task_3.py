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
with open('one_two_tree_four.txt', 'r', encoding='UTF-8') as file:
    text_2 = file.read()
text_1 = text_2
for key, value in my_dict.items():
    text_1 = text_1.replace(key, value)
with open('один_два_три_черыре.txt', 'w', encoding='UTF-8') as file2:
    file2.write(text_1)
