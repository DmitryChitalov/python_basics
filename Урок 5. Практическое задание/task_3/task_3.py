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
NUMBER_DICT = {'One': 'Один',
               'Two': 'Два',
               'Three': 'Три',
               'Four': 'Четыре'}

test_text = open('one_two.txt', 'r', encoding='utf-8')
new_text = open('new_one_two.txt', 'w', encoding='utf-8')
for line in test_text:
    for word in line.split():
        if word in NUMBER_DICT.keys():
            new_text.write(NUMBER_DICT[word] + ' ')
        else:
            new_text.write(word + ' ')
    new_text.write('\n')
test_text.close()
new_text.close()

