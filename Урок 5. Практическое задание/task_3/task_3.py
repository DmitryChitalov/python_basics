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

numbers = {'one': 'Один', 'two': 'Два', 'three': 'Три', 'four': 'Четыре', 'five': 'Пять', 'six': 'Шесть',
           'seven': 'Семь', 'eight': 'Восемь', 'nine': 'Девять'}

if __name__ == '__main__':
    try:
        new_format = []
        with open('en_file.txt', 'r+', encoding='utf-8') as string_obj:
            for i in string_obj:
                for el in i.split():
                    if el.lower() in numbers:
                        new_format.append(i.replace(el, numbers.get(el.lower())))
        with open('ru_file.txt', 'w', encoding='utf-8') as string_obj2:
            string_obj2.writelines(new_format)
    except Exception as e:
        print(e)
