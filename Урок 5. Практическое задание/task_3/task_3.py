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
DELIMITER = " — "

translate_dictionary = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}


def translate_word(trans_word):
    return translate_dictionary[trans_word]


read_file = open("my_read_file.txt", "r")
write_file = open("my_translated_file.txt", "w")
line_number = 0
for read_line in read_file.readlines():
    if read_line != "\n":
        array_words = read_line.split(DELIMITER)
        write_file.write(translate_word(array_words[0]) + DELIMITER + array_words[1])

read_file.close()
write_file.close()
