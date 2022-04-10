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
my_file_for_write = open("my_file05_03_02.txt", 'w', encoding='UTF8')


def my_translator(eng_word):
    my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    rus_word = my_dict.get(eng_word)
    return rus_word


with open("my_file05_03_01.txt", "r", encoding='UTF8') as my_file_for_read:
    for my_row in my_file_for_read:
        my_words = my_row.split(" ")
        my_file_for_write.write(my_row.replace(my_words[0].replace('\n', ''), my_translator(my_words[0])))

my_file_for_write.close()
