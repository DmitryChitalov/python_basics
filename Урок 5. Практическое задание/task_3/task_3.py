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

numbers = {'one':'один', 'two':'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'zero': 'ноль'}

if __name__ == '__main__':
    try:
        with open('text', 'r+') as f_obj:
            new_text = []
            for i in f_obj:
                for el in i.split():
                    if el.lower() in numbers:
                        new_text.append(i.replace(el, numbers.get(el.lower())))
            f_obj.seek(0)
            f_obj.writelines(new_text)
    except IOError:
        print('Warning: error input output')
    except Exception as e:
        print(e)
