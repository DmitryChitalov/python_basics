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


def replace_word(some_str):
    words_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'ЧЕТЫРЕ', 'Five': 'Пять', 'Six': 'Шесть',
                  'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Ноль', }
    result_str = ""
    word = ""
    for el in some_str:
        if el != " ":
            word = word + el
        else:
            if word in words_dict:
                result_str = words_dict[word] + some_str[len(word):]
                word = ""
    return result_str


input_file = open('inputtextfile.txt', 'r')
output_file = open('outputtextfile.txt', 'w+')

for line in input_file:
    tmp = replace_word(line)
    print(tmp)
    output_file.write(replace_word(line))

input_file.close()
output_file.close()
