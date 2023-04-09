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
traslation_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

def translator(file_name, traslation_dict, new_file_name):
    translated_text = []
    with open(file_name, 'r') as orig_file:
        for line in orig_file:
            line_splited = line.split(' ')
            translated_line = []
            for word in line_splited:
                if word in traslation_dict.keys():
                    translated_line.append(traslation_dict[word])
                else:
                    translated_line.append(word)
            translated_line = "".join(translated_line)
            translated_text.append(translated_line+'\n')
    with open(new_file_name, 'a') as output_file:
        output_file.writelines(translated_text)

translator('file.txt', traslation_dict, 'translated_text.txt')
