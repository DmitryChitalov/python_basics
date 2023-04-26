__author__ = 'AndreiM'
__version__ = "1.0 18.04.2023"
print("\n task_3 \n -------- \n")

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


# Google to translate ...
'''
$ pip3 install googletrans (don't forget to install)
from googletrans import Translator
...Translator().translate(text, dest='ru').text
YANDEX
$ pip3 install requests (don't forget to install)
>>> eng_text = 'text for translate'
>>> token = <Yandex-API-key>
>>> url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
>>> trans_option = {'key':token, 'lang':'en-ru', 'text': eng_text}
>>> webRequest = requests.get(url_trans, params = trans_option)
>>> webRequest.text
'{"code":200,"lang":"en-ru","text":["текст для перевода"]}'
>>> rus_text = webRequest.text
>>> rus_text = rus_text[36:(len(rus_text)-3)]
>>> rus_text
'текст для перевода'
'''

# Vers.1
fileold = 'text_3.txt'
'''
One - 1
Two - 2
Three - 3
Four - 4
'''
filenew = 'text_3new.txt'

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
try:
    with open(fileold, 'r') as f:
        for i in f:
            i = i.split(' ', 1)
            new_file.append(rus[i[0]] + ' ' + i[1])
        print(new_file)

    with open(filenew, 'w+', encoding='utf-8') as f:
        f.writelines(new_file)

except FileNotFoundError:
    print(f'Error. Невозможно создать или открыть файл')


# Vers. 2
# Google to translate ...

from googletrans import Translator

fileold = 'text_3.txt'
'''
One - 1
Two - 2
Three - 3
Four - 4
'''
filetotranslate = 'text_3_translate.txt'

try:
    with open(filetotranslate, 'w', encoding='utf-8') as f:
        with open(fileold, 'r', encoding='utf-8') as f1:
            text = f1.read()
        f.write(Translator().translate(text, dest='ru').text)
        print(f'Translated... in file {filetotranslate}')

except FileNotFoundError:
    print(f'Error. Невозможно создать или открыть файл')