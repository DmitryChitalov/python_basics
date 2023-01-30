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
replace_word = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("number_list.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in replace_word.keys():
            line = line.replace(key, replace_word[key])
        print(line)
        with open("new_number_list.txt", 'a', encoding='utf-8') as rus_word:
            rus_word.writelines(f"\n {line}")