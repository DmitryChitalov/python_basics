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
translate = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}
text = []
try:
    with open("new_file.txt", 'r', encoding='utf-8') as file1:
        text = file1.readlines()
        for line in text:
            for word in line.split():
                if word in translate:
                    text[text.index(line)] = line.replace(word, translate.get(word))
        '''
        for line in text:
            words = line.split()
            for word in words:
                if word in translate:
                    words[words.index(word)] = translate.get(word)
            text[text.index(line)] = ' '.join(words)+'\n'
        '''
    with open("out_file.txt", 'w') as file2:
        file2.writelines(text)
except IOError:
    print("Ошибка ввода-вывода!")
